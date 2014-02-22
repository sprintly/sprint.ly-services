import logging
from lookout.base import ServiceBase
import pinder

logger = logging.getLogger(__name__)

class Service(ServiceBase):
    """
    Campfire

    This will send item events from Sprint.ly to your Campfire chat room. To install
    the package follow the steps below:

    1. `subdomain` is Campfire subdomain (e.g. `foobar` in `https://foobar.campfirenow.com`)
    2. `room` is the actual name of the room from your Campfire Lobby. **NOTE:** It is not the ID of the room.
    3. `token` is your Campfire API token. You can find this by clicking the "My info" link next to the "Settings" tab.
    """
    def send(self, payload):
        campfire = pinder.Campfire(self.options['subdomain'], self.options['token'])
        room = campfire.find_room_by_name(self.options['room'])
        if room is None:
            logger.error("Could not join the room %s to send payload %r Options: %r",
                         self.options['room'], payload, self.options)
            return

        if payload['model'] == 'Comment':
            message = '%s %s. commented "%s" on %s "%s" (#%s) %s' % (
                payload['attributes']['created_by']['first_name'],
                payload['attributes']['created_by']['last_name'][0],
                '%s...' % payload['attributes']['body'][0:50], 
                payload['attributes']['item']['type'],
                payload['attributes']['item']['title'],
                payload['attributes']['item']['number'],
                payload['attributes']['item']['short_url'])
        elif payload['model'] == 'Item':
            message = '%s %s. created the %s "%s" (#%s) %s' % (
                payload['attributes']['created_by']['first_name'],
                payload['attributes']['created_by']['last_name'][0],
                payload['attributes']['type'],
                payload['attributes']['title'],
                payload['attributes']['number'],
                payload['attributes']['short_url'])

            if payload['attributes']['assigned_to'] and \
                payload['attributes']['assigned_to']['id'] != \
                payload['attributes']['created_by']['id']:
                message += ' and assigned it to %s %s.' % (
                    payload['attributes']['assigned_to']['first_name'],
                    payload['attributes']['assigned_to']['last_name'][0])
        elif payload['model'] == 'Block':
            message = '%s %s. indicated the %s "%s" (#%s) %s is blocked on the %s "%s" (#%s) %s' % (
                payload['attributes']['user']['first_name'],
                payload['attributes']['user']['last_name'][0],
                payload['attributes']['blocked']['type'],
                payload['attributes']['blocked']['title'],
                payload['attributes']['blocked']['number'],
                payload['attributes']['blocked']['short_url'],
                payload['attributes']['item']['type'],
                payload['attributes']['item']['title'],
                payload['attributes']['item']['number'],
                payload['attributes']['item']['short_url'])

            if payload['attributes']['item']['assigned_to']:
                message += ', which is owned by %s %s.' % (
                    payload['attributes']['item']['assigned_to']['first_name'],
                    payload['attributes']['item']['assigned_to']['last_name'][0])
        elif payload['model'] == 'Favorite':
            message = '%s %s. favorited the %s "%s" (#%s) %s' % (
                payload['attributes']['user']['first_name'],
                payload['attributes']['user']['last_name'][0],
                payload['attributes']['item']['type'],
                payload['attributes']['item']['title'],
                payload['attributes']['item']['number'],
                payload['attributes']['item']['short_url'])
        elif payload['model'] == 'Deploy':
            message = '%s %s. deployed %s items to %s.' % (
                payload['attributes']['user']['first_name'],
                payload['attributes']['user']['last_name'][0],
                len(payload['attributes']['items']),
                payload['attributes']['environment'])
        else:
            message = None

        if not message:
            return

        room.join()
        result = room.speak(message)

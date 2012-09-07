from lookout.base import ServiceBase
import requests

class Service(ServiceBase):
    """
    HipChat 

    This will send item events from Sprint.ly to your HipChat chat room. To install
    the package follow the steps below:

    1. `auth_token` is a valid HipChat API auth token. You can create an `auth_token` at `https://your-domain.hipchat.com/admin/api`.
    2. `room_id` is the actual name of the room from your HipChat Lobby. **NOTE:** It is not the ID of the room.
    """
    def send(self, payload):
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

        data = {
            'auth_token': self.options['auth_token'],
            'format': 'json',
            'room_id': self.options['room_id'],
            'from': 'Sprint.ly',
            'message': message,
            'message_format': 'text',
        }

        url = 'https://api.hipchat.com/v1/rooms/message'
        r = requests.post("https://api.hipchat.com/v1/rooms/message", data=data)

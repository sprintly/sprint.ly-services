import logging

import pinder

from lookout.base import MessageServiceBase, ServiceBase


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

        message = MessageServiceBase.message(payload)
        if not message:
            return

        room.join()
        room.speak(message)
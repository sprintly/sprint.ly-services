import requests

from lookout.base import ServiceBase


class Service(ServiceBase):
    """
    HipChat

    This will send item events from Sprint.ly to your HipChat chat room. To install
    the package follow the steps below:

    1. `auth_token` is a valid HipChat API auth token. You can create an `auth_token` at `https://your-domain.hipchat.com/admin/api`.
    2. `room_id` is the actual name of the room from your HipChat Lobby. **NOTE:** It is not the ID of the room.
    """
    def send(self, payload):
        message = self.get_message(payload)
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
        _ = requests.post(url, data=data)

from pprint import pprint

from mock import patch, Mock

from lookout.services.campfire import Service as CampfireService
from lookout.services.flowdock import Service as FlowdockService
from lookout.services.hipchat import Service as HipchatService
from lookout.services.webhook import Service as WebhookService


# Fixture data

fake_comment_payload = {
    'model': 'Comment',
    'attributes': {
        'created_by': {
            'first_name': 'Peter',
            'last_name': 'Gibbons'
        },
        'item': {
            'type': 'story',
            'title': 'Chotchkies',
            'number': 1,
            'short_url': 'http://sprint.ly'
        },
        'body': "There's a pretty hot waitress over there..."
    }
}


# Tests

def test_campfire_sends():
    options = {
        'subdomain': 'somesub',
        'token': 'sometoken',
        'room': 'someroom'
    }

    with patch('pinder.Campfire') as mock_campfire:
        mock_campfire_room = Mock()
        
        mock_campfire_instance = mock_campfire.return_value
        mock_campfire_instance.find_room_by_name.return_value = mock_campfire_room

        service = CampfireService(options)
        service.send(fake_comment_payload)

        mock_campfire.assert_called_with(options['subdomain'], options['token'])
        mock_campfire_instance.find_room_by_name.assert_called_with(options['room'])

        assert mock_campfire_room.join.called
        assert mock_campfire_room.speak.called

def test_campfire_requires_room():
    pass

def test_flowdock_sends():
    pass

def test_hipchat_sends():
    pass

def test_webhook_sends():
    pass

def test_webhook_requires_urls():
    pass

import pytest

from mock import patch, Mock

from lookout.services.campfire import Service as CampfireService
from lookout.services.flowdock import Service as FlowdockService
from lookout.services.hipchat import Service as HipchatService
from lookout.services.webhook import Service as WebhookService

from .fixtures import all_payloads


# Tests

@pytest.mark.parametrize('payload', all_payloads)
def test_campfire_sends(payload):
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
        service.send(payload)

        mock_campfire.assert_called_with(options['subdomain'], options['token'])
        mock_campfire_instance.find_room_by_name.assert_called_with(options['room'])

        assert mock_campfire_room.join.called
        assert mock_campfire_room.speak.called
        assert type(mock_campfire_room.speak.call_args[0][0]) in [str, unicode]

@pytest.mark.parametrize('payload', all_payloads)
def test_campfire_requires_room(payload):
    options = {
        'subdomain': 'somesub',
        'token': 'sometoken',
        'room': 'someroom'
    }

    with patch('pinder.Campfire') as mock_campfire:
        mock_campfire_room = Mock()
        
        mock_campfire_instance = mock_campfire.return_value
        mock_campfire_instance.find_room_by_name.return_value = None # Fake no room

        service = CampfireService(options)
        service.send(payload)

        assert not mock_campfire_room.join.called
        assert not mock_campfire_room.speak.called

@pytest.mark.parametrize('payload', all_payloads)
def test_flowdock_sends(payload):
    options = {
        'auth_token': 'sometoken'
    }

    with patch('requests.post') as mock_requests_post:
        service = FlowdockService(options)
        service.send(payload)
        assert mock_requests_post.called

@pytest.mark.parametrize('payload', all_payloads)
def test_hipchat_sends(payload):
    options = {
        'auth_token': 'sometoken',
        'room_id': 'someroom'
    }

    with patch('requests.post') as mock_requests_post:
        service = HipchatService(options)
        service.send(payload)
        assert mock_requests_post.called

@pytest.mark.parametrize('payload', all_payloads)
def test_webhook_sends(payload):
    options = {
        'urls': [
            'http://sprint.ly'
        ]
    }

    with patch('urllib2.Request') as mock_urllib2_request:
        with patch('urllib2.urlopen') as mock_urllib2_urlopen:
            mock_request = Mock()
            mock_urllib2_request.return_value = mock_request

            service = WebhookService(options)
            service.send(payload)

            assert mock_urllib2_request.call_count == len(options['urls'])
            mock_urllib2_urlopen.call_args[0][0] == mock_request

@pytest.mark.parametrize('payload', all_payloads)
def test_webhook_requires_urls(payload):
    with patch('urllib2.Request') as mock_urllib2_request:
        with patch('urllib2.urlopen') as mock_urllib2_urlopen:
            mock_request = Mock()
            mock_urllib2_request.return_value = mock_request

            service = WebhookService({})
            service.send(payload)

            assert not mock_urllib2_request.called
            assert not mock_urllib2_urlopen.called

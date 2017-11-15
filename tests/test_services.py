import pytest

from mock import patch, Mock

from lookout.services.flowdock import Service as FlowdockService
from lookout.services.hipchat import Service as HipchatService
from lookout.services.slack import Service as SlackService
from lookout.services.webhook import Service as WebhookService

from .fixtures import all_payloads


# Tests

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
            assert mock_urllib2_request.call_args[0][0] == options['urls'][0]
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

@pytest.mark.parametrize('payload', all_payloads)
def test_slack_sends(payload):
    options = {
        'url': 'https://something.slack.com/services/hooks/incoming-webhook?token=sometoken'
    }

    with patch('urllib2.Request') as mock_urllib2_request:
        with patch('urllib2.urlopen') as mock_urllib2_urlopen:
            mock_request = Mock()
            mock_urllib2_request.return_value = mock_request

            service = SlackService(options)
            service.send(payload)

            assert mock_urllib2_request.called
            assert mock_urllib2_request.call_args[0][0] == options['url']
            mock_urllib2_urlopen.call_args[0][0] == mock_request

@pytest.mark.parametrize('payload', all_payloads)
def test_slack_requires_url(payload):
    with patch('urllib2.Request') as mock_urllib2_request:
        with patch('urllib2.urlopen') as mock_urllib2_urlopen:
            mock_request = Mock()
            mock_urllib2_request.return_value = mock_request

            service = SlackService({})
            service.send(payload)

            assert not mock_urllib2_request.called
            assert not mock_urllib2_urlopen.called


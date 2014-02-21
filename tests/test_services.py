from pprint import pprint

import pytest

from mock import patch, Mock

from lookout.services.campfire import Service as CampfireService
from lookout.services.flowdock import Service as FlowdockService
from lookout.services.hipchat import Service as HipchatService
from lookout.services.webhook import Service as WebhookService


# Fixture data

fake_product = {
    'id': 1,
    'name': 'Sprint.ly'
}

fake_comment_payload = {
    'model': 'Comment',
    'product': fake_product,
    'attributes': {
        'created_by': {
            'id': 1,
            'first_name': 'Peter',
            'last_name': 'Gibbons'
        },
        'item': {
            'id': 1,
            'type': 'story',
            'title': 'Chotchkies',
            'number': 1,
            'short_url': 'http://sprint.ly'
        },
        'body': "Watching kung fu..."
    }
}

fake_item_payload = {
    'model': 'Item',
    'attributes': {
        'created_by': {
            'id': 2,
            'first_name': 'Michael',
            'last_name': 'Bolton'
        },
        'assigned_to': {
            'id': 3,
            'first_name': 'Samir',
            'last_name': 'Nagheenanajar'
        },
        'id': 1,
        'type': 'task',
        'title': 'PC Load Letter',
        'number': 1,
        'short_url': 'http://sprint.ly',
        'body': "What the #$@! does that mean?"
    }
}

fake_block_payload = {
    'model': 'Block',
    'product': fake_product,
    'attributes': {
        'user': {
            'id': 5,
            'first_name': 'Milton',
            'last_name': 'Waddams'
        },
        'item': {
            'id': 1,
            'type': 'defect',
            'title': 'Hogging the stapler',
            'number': 1,
            'short_url': 'http://sprint.ly',
            'assigned_to': {
                'id': 6,
                'first_name': 'Bill',
                'last_name': 'Lumbergh'
            }
        },
        'blocked': {
            'id': 2,
            'type': 'defect',
            'title': 'Stapling a bunch of things',
            'number': 2,
            'short_url': 'http://sprint.ly',
        }
    }
}

fake_favorite_payload = {
    'model': 'Favorite',
    'product': fake_product,
    'attributes': {
        'user': {
            'id': 7,
            'first_name': 'Tom',
            'last_name': 'Smykowski'
        },
        'item': {
            'id': 1,
            'type': 'story',
            'title': 'Jump to Conclusions Mat',
            'number': 1,
            'short_url': 'http://sprint.ly'
        }
    }
}

fake_deploy_payload = {
    'model': 'Deploy',
    'product': fake_product,
    'attributes': {
        'user': {
            'id': 1,
            'first_name': 'Bob Slydell',
            'last_name': 'Gibbons'
        },
        'items': [],
        'environment': "Watching kung fu..."
    }
}

all_payloads = [
    fake_comment_payload,
    fake_item_payload,
    fake_block_payload,
    fake_favorite_payload,
    fake_deploy_payload
]

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
        assert type(mock_campfire_room.speak.call_args[0][0]) == str

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

    with patch('requests') as mock_requests:
        service = FlowdockService(options)
        service.send(payload)
        assert mock_requests.post.called

def test_hipchat_sends():
    pass

def test_webhook_sends():
    pass

def test_webhook_requires_urls():
    pass

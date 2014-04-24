import pytest

from mock import patch

from lookout.services.slack import Service

from .fixtures import all_payloads


def test_get_attachment_color():
    srv = Service({})
    assert type(srv.get_attachment_color({'type': 'story'})) == str

def test_get_attachment_color_empty():
    srv = Service({})
    assert type(srv.get_attachment_color()) == str

def test_format_item_link():
    srv = Service({})
    item = {
        'short_url': '',
        'title': '',
        'number' : 1
    }
    link = srv.format_item_link(item)

    assert type(link) ==  str
    assert link[0] == '<'
    assert link[-1] == '>'

@pytest.mark.parametrize('payload', all_payloads)
def test_get_post_data(payload):
    model = payload['model'].lower()
    srv = Service({})
    with patch.object(srv, 'get_%s_attachment' % model) as mock_get_attachment:
        mock_get_attachment.return_value = {}
        post_data = srv.get_post_data(payload)
        assert post_data.has_key('attachments')
        mock_get_attachment.assert_called_with(payload)

@pytest.mark.parametrize('payload', all_payloads)
def test_get_attachment(payload):
    srv = Service({})
    model = payload['model'].lower()
    method = 'get_%s_attachment' % model
    attachment = getattr(srv, method)(payload)
    assert type(attachment) == dict
    assert attachment.has_key('text')

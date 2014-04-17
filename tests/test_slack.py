from mock import patch

from lookout.services.slack import Service

from .fixtures import fake_item_payload


def test_get_attachment_color():
    srv = Service({})
    assert type(srv.get_attachment_color({'type': 'story'})) == str

def test_get_attachment_color_empty():
    srv = Service({})
    assert type(srv.get_attachment_color()) == str

def test_get_post_data():
    srv = Service({})
    with patch.object(srv, 'get_item_attachment') as mock_get_item_attachment:
        mock_get_item_attachment.return_value = {}
        post_data = srv.get_post_data(fake_item_payload)
        assert post_data.has_key('attachments')
        mock_get_item_attachment.assert_called_with(fake_item_payload)

def test_get_item_attachment():
    srv = Service({})
    attachment = srv.get_item_attachment(fake_item_payload)
    assert type(attachment) == dict
    assert attachment.has_key('text')

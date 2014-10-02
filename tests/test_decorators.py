import mock

from lookout.decorators import listen_to

def test_listen_to_passes_on_events():
    mocked_client = mock.Mock()

    @listen_to('*.created')
    def mocked_service_send(self, payload):
        mocked_client(payload) 

    mocked_service_send(None, {'action': 'created', 'model': 'Foo'})
    assert mocked_client.called


def test_listen_to_works_with_no_action_specified():
    mocked_client = mock.Mock()

    @listen_to('*.created')
    def mocked_service_send(self, payload):
        mocked_client(payload) 

    mocked_service_send(None, {'model': 'Foo'})
    assert mocked_client.called


def test_listen_to_ignores_unspecified_events():
    mocked_client = mock.Mock()

    @listen_to('*.created')
    def mocked_service_send(self, payload):
        mocked_client(payload) 

    mocked_service_send(None, {'action': 'updated', 'model': 'Foo'})
    assert mocked_client.called == False


def test_listen_to_works_with_multiple_patterns():
    mocked_client = mock.Mock()

    @listen_to('*.created', '*.deleted')
    def mocked_service_send(self, payload):
        mocked_client(payload) 

    mocked_service_send(None, {'action': 'created', 'model': 'Foo'})
    assert mocked_client.called

    mocked_client.reset_mock()
    mocked_service_send(None, {'action': 'deleted', 'model': 'Foo'})
    assert mocked_client.called

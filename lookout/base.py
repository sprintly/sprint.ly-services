class ServiceBase(object):
    def __init__(self, options):
        self.options = options

    def send(self, payload):
        raise NotImplementedError

    @property
    def title(self):
        return self.__doc__.split('\n')[1].strip()

    @property
    def description(self):
        return '\n'.join([l.strip() for l in self.__doc__.split('\n')[2:]]).strip()


def get_available_services():
    pass

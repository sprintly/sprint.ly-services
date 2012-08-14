import os
from django.utils.importlib import import_module


class ServiceBase(object):
    def __init__(self, options):
        self.options = options

    def send(self, payload):
        raise NotImplementedError

    @property
    def name(self):
        return self.__class__.__module__.split('.')[-1]

    @property
    def title(self):
        return self.__doc__.split('\n')[1].strip()

    @property
    def description(self):
        return '\n'.join([l.strip() for l in self.__doc__.split('\n')[2:]]).strip()


def get_available_services():
    path = '%s/services' % os.path.dirname(__file__)
    services = {}
    for service_file in os.listdir(path):
        if service_file.endswith('.pyc') or service_file.startswith('__'):
            continue

        service_name = service_file.split('.')[0]

        try:
            module = import_module('lookout.services.%s' % service_name)
            services[service_name] = module.Service
        except ImportError:
            continue

    return services

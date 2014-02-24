import os
import re

from lookout.base import get_available_services, MessageServiceBase


ROOT_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


def test_get_available_services():
    services = get_available_services()
    services_dir = os.path.join(ROOT_DIR, 'lookout', 'services')
    service_file_list = filter(lambda service_file: not re.match('.*\.pyc$', service_file) and not re.match('^__', service_file), os.listdir(services_dir))
    assert len(service_file_list) == len(services)

def test_clean_mentions():
    comment = "Hello there @[Joe Stump](pk:1)"
    assert MessageServiceBase._clean_mentions(comment) == "Hello there Joe Stump"
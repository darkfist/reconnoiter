import os
from domain_name import *


def get_ip_address(url):
    command = "host " + get_domain_name(url)
    process = os.popen(command)
    results = str(process.read())
    marker = results.find("has address") + 12
    return results[marker:].splitlines()[0]

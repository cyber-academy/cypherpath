from cypherpath.rest_api import sdi
from cypherpath.rest_api import tenancy
from cypherpath.rest_api import user
from cypherpath.rest_api import utils

import json

def test_sdi():
    response = sdi.get_sdis()
    print('status_code = {}'.format(response.status_code))
    parsed = json.loads(response.text)
    print('json() = {}'.format(json.dumps(parsed, indent=4, sort_keys=False)))

def test_tenancy():
    response = tenancy.get_tenancies()
    print('status_code = {}'.format(response.status_code))
    parsed = json.loads(response.text)
    print('json() = {}'.format(json.dumps(parsed, indent=4, sort_keys=False)))

def test_start():
    response = sdi.start_sdi("b637ec43-a579-47f2-a308-fb3788feddb6")
    print(response.status_code)

def test_stop():
    response = sdi.stop_sdi("b637ec43-a579-47f2-a308-fb3788feddb6")
    print(response.status_code)

def test_create_machine():
    response = sdi.create_machine()

def test_get_machines():
    response = sdi.get_machines('35e4b14f-1aff-4a5c-be65-03b7e6725bbf')
    print('status_code = {}'.format(response.status_code))
    parsed = json.loads(response.text)
    print('json() = {}'.format(json.dumps(parsed['user'], indent=4, sort_keys=False)))

def test_sdi_status():
    response = sdi.get_sdi_status('4bbbf390-c529-497c-a77f-bd9b6710d9d1')

    print(response)

if __name__ == "__main__":
    test_sdi_status()














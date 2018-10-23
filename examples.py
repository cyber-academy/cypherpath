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


if __name__ == "__main__":
    sdi_id = '0c8bef59-4220-4c18-9d8c-678d46bdec43'
    machine_id = '4f5f1302-98b9-4a85-a8f7-3b2d1131f76c'
    sdi_url = utils.get_vnc_url(sdi_id=sdi_id, machine_id=machine_id, user_id=36)
    print(sdi_url)













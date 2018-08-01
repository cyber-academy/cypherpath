from cypherpath.rest_api import sdi
from cypherpath.rest_api import tenancy
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

if __name__ == "__main__":
    test_stop()












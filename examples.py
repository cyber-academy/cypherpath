from cypherpath.rest_api import user
from cypherpath.rest_api import sdi
from cypherpath.rest_api import tenancy
import json


def test_tenancy():
    response = tenancy.get_tenancies()
    print('status_code = {}'.format(response.status_code))
    parsed = json.loads(response.text)
    print('json() = {}'.format(json.dumps(parsed, indent=4, sort_keys=False)))

if __name__ == "__main__":
    test_tenancy()












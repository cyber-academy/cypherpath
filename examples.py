from cypherpath.rest_api import user
from cypherpath.rest_api import sdi

if __name__ == "__main__":
    response = sdi.get_sdis()
    print('status_code = {}'.format(response.status_code))
    print('text = {}'.format(response.text))
    print('json() = {}'.format(response.json()))









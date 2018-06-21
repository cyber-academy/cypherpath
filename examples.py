from cypherpath.rest_api import user
from cypherpath.rest_api import sdi

if __name__ == "__main__":
    response = sdi.get_sdi_by_user(6)
    print('status_code = {}'.format(response.status_code))
    print('json() = {}'.format(response.json()))

    for r in response.json():
        print(f'{r["name"]} = {r["sdi_id"]}')












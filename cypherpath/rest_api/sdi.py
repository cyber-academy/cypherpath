import requests
import urllib3
urllib3.disable_warnings()
import time

from cypherpath.rest_api.client import Client


def get_sdis():
    client = Client()
    api_url = f'https://{client.url}/api/sdis/'
    response = requests.get(api_url, headers=client.headers, verify=False)
    return response

def get_sdi(sdi_id):
    client = Client()
    api_url = f'https://{client.url}/api/sdis/{sdi_id}'
    response = requests.get(api_url, headers=client.headers, verify=False)
    return response

def copy_sdi(user, copy_from, new_name):
    client = Client()
    post_data = {
        "user": user,
        "name": new_name,
        "desdcription": "this is the description",
        "remove_persistence": 0,
        "deep_copy": 0,
    }
    api_url = f'https://{client.url}/api/sdis/{copy_from}/copy/'
    response = requests.post(api_url, headers=client.headers, data=post_data, verify=False)
    exists = 'An SDI with this name already exists.'
    copying = 'The source SDI is currently being copied.'
    while response.status_code == 400:
        if response.json()[0]['message'] == exists:
            print("The SDI allready exists")
            break

        if (response.json()[0]['message'] == copying):
            print("The SDI is still Copying")
            time.sleep(2)
            response = requests.post(api_url, headers=client.headers, data=post_data, verify=False)

    return response

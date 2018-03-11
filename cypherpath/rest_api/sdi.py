import requests
import urllib3
urllib3.disable_warnings()

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
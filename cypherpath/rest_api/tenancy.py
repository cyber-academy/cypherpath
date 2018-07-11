from cypherpath.rest_api.client import Client
import requests
import urllib3
urllib3.disable_warnings()


def get_tenancies():
    client = Client()
    api_url = f'https://{client.url}/api/accounts/tenancies/'
    response = requests.get(api_url, headers=client.headers, verify=False)
    return response

def get_tenancy():
    pass

def get_tenancy_security():
    pass

def get_tenancy_authentication():
    pass
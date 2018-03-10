import requests
import urllib3
urllib3.disable_warnings()

from cypherpath.rest_api.client import Client


def get_users():
    client = Client()
    api_url = f'https://{client.url}/api/accounts/users/'
    response = requests.get(api_url, headers=client.headers, verify=False)
    return response


def get_user(user_id):
    client = Client()
    api_url = f'https://{client.url}/api/accounts/users/{user_id}'
    response = requests.get(api_url, headers=client.headers, verify=False)
    return response


def get_user_networks(user_id):
    client = Client()
    api_url = f'https://{client.url}/api/accounts/users/{user_id}/networks/'
    response = requests.get(api_url, headers=client.headers, verify=False)
    return response


def get_user_sdis(user_id):
    client = Client()
    api_url = f'https://{client.url}/api/accounts/users/{user_id}/sdis/'
    response = requests.get(api_url, headers=client.headers, verify=False)
    return response


def get_user_disks(user_id):
    client = Client()
    api_url = f'https://{client.url}/api/accounts/users/{user_id}/disks/'
    response = requests.get(api_url, headers=client.headers, verify=False)
    return response


def get_user_single_use_login_token():
    client = Client()
    api_url = f'https://{client.url}/api/accounts/login/token/'
    response = requests.get(api_url, headers=client.headers, verify=False)
    return response


def create_user_single_use_login_token(user_id):
    client = Client()
    post_data = {
        "user": user_id
    }
    api_url = f'https://{client.url}/api/accounts/login/token/'
    response = requests.post(api_url, headers=client.headers, data=post_data,
                             verify=False)
    return response


def create_user(username, password, tenancy=1):
    client = Client()
    post_data = {
        "username": username,
        "password": password,
        "tenancy": tenancy,
        "is_active": 1
    }
    api_url = f'https://{client.url}/api/accounts/users/'
    response = requests.post(api_url, headers=client.headers, data=post_data, verify=False)
    return response

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


def get_sdi_status(sdi_id):
    client = Client()
    api_url = f'https://{client.url}/api/sdis/{sdi_id}'
    response = requests.get(api_url, headers=client.headers, verify=False).json()
    state = ""
    status = response.get('status')
    if status:
        state = response['status']['state']
        if state == 0:
            state = "stopped"
        elif state == 1:
            state = "starting"
        elif state == 2:
            state = "running"
        elif state == 3:
            state = "stopping"
    else:
        state = "error"

    return {'state': state}


def get_sdi_overview(sdi_id):
    client = Client()
    api_url = f'https://{client.url}/api/sdis/{sdi_id}/overview'
    response = requests.get(api_url, headers=client.headers, verify=False)
    return response


def get_sdi_by_user(user_pk):
    client = Client()
    api_url = f'https://{client.url}/api/sdis/{user_pk}'
    response = requests.get(api_url, headers=client.headers, verify=False)
    return response


def stop_sdi(sdi_id):
    client = Client()
    api_url = f'https://{client.url}/api/sdis/{sdi_id}/stop'
    response = requests.post(api_url, headers=client.headers, verify=False)
    return response


def start_sdi(sdi_id):
    client = Client()
    api_url = f'https://{client.url}/api/sdis/{sdi_id}/start'
    response = requests.post(api_url, headers=client.headers, verify=False)
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


def delete_sdi(sdi_id):
    client = Client()
    api_url = f'https://{client.url}/api/sdis/{sdi_id}'
    response = requests.delete(api_url, headers=client.headers, verify=False)
    return response


# {
#     "id": "60f567d8-8d95-4777-9988-448dd009ac2c",
#     "name": "hyperqube-ubuntu18.04-00001",
#     "description": "",
#     "memory": 4096,
#     "sockets": 1,
#     "cores": 1,
#     "threads": 1,
#     "boot_priority": null,
#     "role": "workstation",
#     "image_persist": true,
#     "datetime": null,
#     "boot_device": "disk",
#     "boot_menu": 0,
#     "cpu_type": "qemu64",
#     "video_card": "vmware",
#     "bios_manufacturer": "",
#     "drives": [
#         {
#             "master_id": "0b230b6a-4d40-4c92-a9b2-d771d959eb8a",
#             "master_name": "hyperqube-ubuntu18.04",
#             "bus": "ide"
#         },
#         {
#             "master_id": null,
#             "master_name": "<Ejected CD-ROM>",
#             "bus": "ide"
#         }
#     ],
#     "snapshots": null,
#     "vnc_data": null,
#     "status": null,
#     "interfaces": [
#         {
#             "id": "9c9a0f04-1286-4475-9a1c-f7c483201c61",
#             "network": "1d8bce5e-bdc2-44ee-821a-8787d92ee667",
#             "nic": "e1000",
#             "mac": "52:54:00:b5:cc:cc",
#             "hostname": null,
#             "vlan_mode": "native-untagged",
#             "vlan_pvid": 1,
#             "vlans": [
#                 {
#                     "vlan": 1,
#                     "ip": "10.1.0.1",
#                     "ipv6": "[]"
#                 }
#             ]
#         }
#     ],
# }


def create_machine(sdi_id, name, memory, sockets, cores, role):
    client = Client()
    api_url = f'https://{client.url}/api/sdis/{sdi_id}/machines/'
    post_data = {
        "name": name,
        "description": "",
        "memory": memory,
        "sockets": sockets,
        "cores": cores,
        "threads": 1,
        "role": role,
        "boot_device": "disk",
        "boot_menu": 0,
        "cpu_type": "qemu64",
        "video_card": "vmware",
        "bios_manufacturer": "",
    }
    response = requests.post(api_url, headers=client.headers, data=post_data, verify=False)
    return response


def get_machines(sdi_id):
    client = Client()
    api_url = f'https://{client.url}/api/sdis/{sdi_id}/machines/'
    response = requests.get(api_url, headers=client.headers, verify=False)
    return response

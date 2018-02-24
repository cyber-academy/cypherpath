from cypherpath import rest_api
import time

# get_users
def get_users_example():
    client = rest_api.Client()
    users = client.get_users()
    print(users)


def create_user_example():
    client = rest_api.Client()
    u = 'test_user_01'
    p = 'password'
    client.create_user(username=u, password=p)
    print(client.get_usernames())


def get_user_by_username_example():
    client = rest_api.Client()
    username = "student"
    print(client.get_user_by_username(username))


def get_sdi_url_example():
    user_id = "37"
    sdi_id = "6631f00b-16ff-42fe-a47f-3a7a9a2f6b8f"
    client = rest_api.Client()
    response = client.get_sdi_url(user_id=user_id, sdi_id=sdi_id)
    print(response)

def get_sdi_status_example():
    sdi_id = "59c75da4-8668-4aac-9971-40d5434134ff"
    client = rest_api.Client()
    response = client.get_sdi_status(sdi_id=sdi_id)
    print(response)

def get_vnc_url_example():
    sdi_id = 'bb2c9a0b-426f-4bd6-b239-f74696c6bf8c'
    vm_id = '1dad688a-43a8-44da-9f15-8796563ae4c4'
    user_id = "43"
    client = rest_api.Client()
    print(client.get_vnc_url(user_id=user_id, sdi_id=sdi_id, vm_id=vm_id))

if __name__ == "__main__":
    get_vnc_url_example()









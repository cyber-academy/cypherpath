import os
import requests
import urllib3
urllib3.disable_warnings()
import time


class Client(object):
    def __init__(self, client_id=None, client_secret=None, cypherpath_username=None, 
                 cypherpath_password=None, cypherpath_url=None):
        
        self.client_id = client_id or os.getenv('CLIENT_ID', None)
        self.client_secret = client_secret or os.getenv('CLIENT_SECRET', None)
        self.username = cypherpath_username or os.getenv('CYPHERPATH_USERNAME', None)
        self.password = cypherpath_password or os.getenv('CYPHERPATH_PASSWORD', None)
        self.url = cypherpath_url or os.getenv('CYPHERPATH_URL', None)
        
        if not self.client_id: raise ValueError('CLIENT_ID not set')
            
        if not self.client_secret: raise ValueError('CLIENT_SECRET not set')
        
        if not self.username: raise ValueError('CYPHERPATH_USERNAME not set')
        
        if not self.password: raise ValueError('CYPHERPATH_PASSWORD not set')
        
        if not self.url: raise ValueError('CYPHERPATH_URL not set')
        
        post_data = {'grant_type':'password', 'username':self.username, 'password':self.password}
        oauth_url = 'https://{}:{}@{}/api/o/token/'.format(self.client_id, self.client_secret, self.url)
        
        response = requests.post(oauth_url, data=post_data, verify=False)
        self.access_token= response.json()['access_token']
        self.headers = {'Authorization':'Bearer {}'.format(self.access_token)}
    
    def get_users(self):
        api_url = 'https://{}/api/accounts/users/'.format(self.url)
        response = requests.get(api_url, headers=self.headers, verify=False)
        return response.json()

    def get_usernames(self):
        names = []
        users = self.get_users()
        for u in users:
            names.append(u['username'])
        return names

    def get_user_by_username(self, username):
        users = self.get_users()
        for user in users:
            if user['username'] == username:
                return user

    def create_user(self, username, password, tenancy=1):
        post_data = {
            "username":username, 
            "password":password, 
            "tenancy":tenancy,
            "is_active":1
        }
        api_url = 'https://{}/api/accounts/users/'.format(self.url)
        response = requests.post(api_url, headers=self.headers, data=post_data, verify=False)
        return response
    
    def get_user_sdis(self, primary_key):
        pass

    def get_sdis(self):
        api_url = 'https://{}/api/sdis/'.format(self.url)
        return requests.get(api_url, headers=self.headers, verify=False).json()

    def get_sdi_details(self, sdi_id):
        api_url = 'https://{}/api/sdis/{}'.format(self.url, sdi_id)
        return requests.get(api_url, headers=self.headers, verify=False).json()

    def get_sdi_status(self, sdi_id):
        api_url = 'https://{}/api/sdis/{}'.format(self.url, sdi_id)
        return requests.get(api_url, headers=self.headers, verify=False).json()['status']

    def get_virtual_machines(self, sdi_id):
        api_url = 'https://{}/api/sdis/{}/machines/'.format(self.url,sdi_id)
        response = requests.get(api_url, headers=self.headers, verify=False).json()

        return response['user']

    def get_vnc_url(self, user_id, sdi_id, vm_id):
        'https://srv1.cyberacademy.us/sdi/6631f00b-16ff-42fe-a47f-3a7a9a2f6b8f/topology/machine/1dad688a-43a8-44da-9f15-8796563ae4c4/vnc/'
        vnc_url = 'https://{}/sdi/{}/topology/machine/{}/vnc'.format(self.url, sdi_id, vm_id)
        return vnc_url




    def copy_sdi(self, user, copy_from, new_name ):
        post_data = {
            "user":user,
            "name":new_name,
            "desdcription":"this is the description",
            "remove_persistence":0,
            "deep_copy":0,
        }
        api_url = 'https://{}/api/sdis/{}/copy/'.format(self.url, copy_from)
        response = requests.post(api_url, headers=self.headers, data=post_data, verify=False)
        exists = 'An SDI with this name already exists.'
        copying = 'The source SDI is currently being copied.'
        while (response.status_code == 400):
            if (response.json()[0]['message'] == exists):
                print("The SDI allready exists")
                break

            if (response.json()[0]['message'] == copying):
                print("The SDI is still Copying")
                time.sleep(2)
                response = requests.post(api_url, headers=self.headers, data=post_data, verify=False)

        return response
        
    def get_sdi_url(self, user_id, sdi_id):
        post_data = {
            "user":user_id
        }
        api_url = 'https://{}/api/accounts/login/token'.format(self.url)
        response = requests.post(api_url, headers=self.headers, data=post_data, verify=False)
        response_url = "{}?next=/sdi/{}/topology_view/".format(response.json()["url"], sdi_id)
        return response_url

if __name__ == "__main__":
    pass

import os
import requests
import urllib3
urllib3.disable_warnings()

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
        print(response)
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

    def get_user(self, primary_key):
        pass

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
        
    def get_virtual_machines(self, sdi_id):
        api_url = 'https://{}/api/sdis/{}/machines/'.format(self.url,sdi_id)
        return requests.get(api_url, headers=self.headers, verify=False).json()['user']
        
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
        return response
        
if __name__ == "__main__":
    client = Client()
    response = client.copy_sdi(1,"d20c09fd-94c4-4ec3-a1e7-1de195aa97fd","new_sdi_01",)
    print(response.status_code)
    print(response.text)
    print(response.url)
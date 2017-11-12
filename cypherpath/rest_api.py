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
        self.access_token= response.json()['access_token']
        self.headers = {'Authorization':'Bearer {}'.format(self.access_token)}
    
    def get_users(self):
        api_url = 'https://{}/api/accounts/users/'.format(self.url)
        return requests.get(api_url, headers=self.headers, verify=False).json()

    def get_user(self, primary_key):
        pass

    def create_user(self, username, password, tenancy=1):
        post_data = {"username":username, 
                     "password":password, 
                     "tenancy":tenancy,
                     "is_active":1}
        api_url = 'https://{}/api/accounts/users/'.format(self.url)
        response = requests.post(api_url, headers=self.headers, data=post_data, verify=False)
        return response
    
    def get_user_sdis(self, primary_key):
        pass

    def get_sdis(self):
        api_url = 'https://{}/api/sdis/'.format(self.url)
        return requests.get(api_url, headers=self.headers, verify=False).json()

if __name__ == "__main__":
   client = Client()
   response = client.create_user("test_account_2", "Password_1")
   print(response.text)
   
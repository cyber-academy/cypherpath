from cypherpath import rest_api

#get_users
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
    username = "hacked_student"
    print(client.get_user_by_username(username))

def get_sdi_url_example():
	user_id = "37"
	sdi_id = "991eaa90-ca58-4f67-8719-2ab773bb5cdc"
	client = rest_api.Client()
	response = client.get_sdi_url(user_id=user_id, sdi_id=sdi_id)
	print(response)

if __name__ == "__main__":
	get_sdi_url_example()
	


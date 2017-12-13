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

if __name__ == "__main__":
	create_user_example()


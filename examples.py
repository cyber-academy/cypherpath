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
        username = "fundamentals_of_cyber"
        print(client.get_user_by_username(username))

if __name__ == "__main__":
	get_user_by_username_example()
	


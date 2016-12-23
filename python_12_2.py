# _*_ coding: utf-8 _*_
import facebook

token = 'EAACEdEose0cBACrHLNB0qKhgpKNe7HZCDHucjIFwNiZCvi1TvXbvjRI484tSyM4Y0XwfyYDTtbzVQDOOOUCosvDHeZAa5nPTN5xzY0NZBzjtybFxNLA5cxbaBCnujVreGPSYlCJlPPSZC1iNRQUDcgxHg0YCiU2AOKLDzC4J16QZDZD'
g = facebook.GraphAPI(access_token=token)

posts = g.get_connections(id='me', connection_name='posts')
posts = posts['data']

for p in posts:
	if 'likes' in p and 'message' in p:
		print('\n',p['created_time'], '的')
		print('訊息:',p['message'])
		likes = p['likes']['data']
		print('共有',len(likes), '人按讚,分別是:')
		for like in likes:
			print(like['name'],)
		print('\n--------------------------------')
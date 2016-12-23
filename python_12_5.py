# _*_ coding: utf-8 _*_

import facebook, shutil, requests

token = 'EAACEdEose0cBANXduaJ0ZBm8mZCeDWuDNq9wxPtZA0SYcnpQKtWa2q1bFup1nboCVWeZCeuqzY7RJ3Q1ZAXYt0ZBqmaG1MqJZCu9aDTJO6vjGTSZCDlhIBcnqsxJhFshiRoP9A5G7sPA6AEd138n27W43FSYZA4qbrtQRU8ZCYW7ZChZCQZDZD'

g = facebook.GraphAPI(access_token=token)

photos = g.get_connections(id='me', connection_name='photos')
photos = photos['data']

for p in photos:
	image = p['images'][0]
	filename = image['source'].split('/')[-1].split('?')[0]
	print(filename)
	fp = open('fb-images'+filename, 'wb')
	pic = requests.get(image['source'], stream=True)
	shutil.copyfileobj(pic.raw, fp)
	fp.close()
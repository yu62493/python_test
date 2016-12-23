# _*_ coding: utf-8 _*_

import requests , json

url = "https://graph.facebook.com/v2.8/me/posts?access_token=EAACEdEose0cBAFeHaqYXV8ZAZCsGeBLgyQ5sGYzSOg3vVw8AGIjqydZAOaEF9fgnFBoXNeC609ivLzUhvbZBpMeGZAwBRIUQzkJ1p4z92kVLuicXS8lA1Y7ZBbKoxIWL0rLWrxQJPEoTKf6bdrkQwli6cSQ4F8N1aQUUVnnk8p2wZDZD"

res = requests.get(url)

data = json.loads(res.text)
for d in data['data']:
	if 'message' in d:
		print(d['created_time'], ':', d['message'])
		print('-----------------------------------')
# _*_ coding: utf-8 _*_

import facebook

token = 'EAACEdEose0cBANXduaJ0ZBm8mZCeDWuDNq9wxPtZA0SYcnpQKtWa2q1bFup1nboCVWeZCeuqzY7RJ3Q1ZAXYt0ZBqmaG1MqJZCu9aDTJO6vjGTSZCDlhIBcnqsxJhFshiRoP9A5G7sPA6AEd138n27W43FSYZA4qbrtQRU8ZCYW7ZChZCQZDZD'

g = facebook.GraphAPI(access_token=token)

attachment = {
	'name': 'Tiny Test',
	'link': 'http://www.yusco.com.tw',
	'caption': '燁聯鋼鐵',
	'description': '燁聯鋼鐵公司網站,國內第一大不鏽鋼公司'
}

g.put_wall_post(message='Python facebook-sdk TEST', attachment=attachment )
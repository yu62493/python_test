# _*_ coding: utf-8 _*_

from firebase import firebase
import time


new_users = [
{'name':'Tiny'},
{'name':'Lily'},
{'name':'Doren'},
{'name':'Bonne'}
]

db_url = 'https://tinyfirebase.firebaseio.com/'
fdb = firebase.FirebaseApplication(db_url, None)
for user in new_users:
	fdb.post('/user',user)
	time.sleep(3)
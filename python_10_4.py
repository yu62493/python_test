# _*_ coding: utf-8 *_*

import json, requests, hashlib, datetime, os.path, sqlite3

url = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_week.geojson'
r = requests.get(url)
sig = hashlib.md5(r.text.encode('utf-8')).hexdigest()
old_sig = ''

if os.path.exists('eq_sig.txt'):
	with open('eq_sig.txt', 'r') as fp:
		old_sig = fp.read()
	with open('eq_sig.txt', 'w') as fp:
		fp.write(sig)
else:
	with open('eq_sig.txt', 'w') as fp:
		fp.write(sig)

if sig == old_sig:
	print('資料未更新,不需處理.....')
	exit()

eqrthquakes = json.loads(r.text)
dataset = list()
for eq in eqrthquakes['features']:
	item = dict()
	eptime = float(eq['properties']['time']) / 1000.0
	d = datetime.datetime.fromtimestamp(eptime). \
	strftime('%Y-%m-%d %H:%M:%S')
	item['eqtime'] = d
	item['mag'] = eq['properties']['mag']
	item['place'] = eq['properties']['place']
	dataset.append(item)

conn = sqlite3.connect('c:\\sqlite3\\earthquakes')
sqlstr = "delete from eq"
conn.execute(sqlstr)
conn.commit()

for data in dataset:
	sqlstr = "insert into eq values('{}',{},'{}');".format(data['eqtime'],data['mag'],data['place'].replace("'",""))
	print(sqlstr)
	conn.execute(sqlstr)
	conn.commit()

print('資料更新完成')
conn.close()

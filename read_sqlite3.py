import sqlite3
conn = sqlite3.connect('c://sqlite3/tiny.db')
cursor = conn.execute('select * from test;')
for row in cursor:
	print('No {}: {}'.format(row[0],row[1]))

conn.close()
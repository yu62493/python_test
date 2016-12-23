import pyodbc

cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-NIVQJDB\SQLEXPRESS;DATABASE=TINY;UID=yu62493;PWD=yu62493')
cursor = cnxn.cursor()

try:	
	cursor.execute("select * from Employees")
	for row in cursor:
		print(row[1])
except:
	print('Error : unable to fetch data')

cnxn.close()
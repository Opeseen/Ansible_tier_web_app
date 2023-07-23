import mysql.connector

try:
    mydb = mysql.connector.connect(
        host="vprodb",
		user="root",
		password="admin1234"
	)
    print('DATABASE CONNECTED')
except Exception as e:
    print('THERE WAS AN ERROR')
    print(e)
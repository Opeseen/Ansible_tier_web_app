import mysql.connector

try:
    mydb = mysql.connector.connect(
        host="vprodb",
		user="root",
		password="admin1234"
	)
    print('DATABASE CONNECTED')
    
    mycursor = mydb.cursor()
    mycursor.execute("SHOW DATABASES")

    for x in mycursor:
        print(x)
except Exception as e:
    print('THERE WAS AN ERROR')
    print(e)
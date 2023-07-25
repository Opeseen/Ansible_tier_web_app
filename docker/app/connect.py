import mysql.connector

try:
    mydb = mysql.connector.connect(
        host="vprodb",
		user="horpe",
		password="mundial"
	)
    print('DATABASE CONNECTED')
    
    mycursor = mydb.cursor()
    mycursor.execute("SHOW DATABASES")

    for x in mycursor:
        print(x)
except Exception as e:
    print('THERE WAS AN ERROR')
    print(e)
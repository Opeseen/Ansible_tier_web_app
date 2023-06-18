import mysql.connector;
from mysql.connector import Error;

try:
    connection = mysql.connector.connect(
    host = "python-flaskdb.cfzrgfw3zego.us-east-1.rds.amazonaws.com",
    user = "admin",
    password = "admin1234",
    database='tododb'
)
    print("MySQL Database connection successful")
except Error as err:
    print(f"Error: '{err}'")
import mysql.connector;
from mysql.connector import Error;
import config;

try:
    connection = mysql.connector.connect(
    host = config.dbendpoint,
    user = config.dbuser,
    password = config.dbpass,
    database= config.dbname
)
    print("MySQL Database connection successful")
except Error as err:
    print(f"Error: '{err}'")
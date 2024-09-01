import mysql.connector as sql_connector
from mysql.connector import Error

try:
    database = sql_connector.connect(
        host="localhost", port="3307", user="danargh", passwd="12345"
    )

    if database.is_connected():
        print("Connected to mysql")

        # use agar cursor ditutup secara otomatis setelah digunakan
        with database.cursor() as cursor_object:
            # create database
            cursor_object.execute("CREATE DATABASE IF NOT EXISTS db_mvc_django")
            print("Database sucessfully created")

except Error as error:
    print(f"Error: {error}")

finally:
    if database.is_connected():
        database.close()
        print("Database connection is closed")

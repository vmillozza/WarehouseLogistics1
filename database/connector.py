import mysql.connector
import os
# Connect to MySQL database
def doconnect():

    try:
        connection = mysql.connector.connect(
            host=os.getenv('hostname'),
            user=os.getenv('username'),
            password=os.getenv('password'),
            database=os.getenv('database')
        )

        if connection.is_connected():
           

            
            
            print("Tables created successfully")
            return True

    except mysql.connector.Error as error:
        print(f"Failed to create table in MySQL: {error}")
    finally:
        if connection.is_connected():
            #cursor.close()
            connection.close()
            print("MySQL connection is closed")
    
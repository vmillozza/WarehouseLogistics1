import mysql.connector
import os
import logging
# Connect to MySQL database


def fetch_data_from_utente(user,password):
    # Configuration details for the MySQL connection
    config = {
        "host": "localhost",
        "user": "root",
        "password": "",
        "database": "dbwarehouse"
    }

    # Establish a connection to the MySQL database
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    try:
        # Execute the SQL query
        query = 'SELECT * FROM Utenti WHERE username = ? AND password = ?', (user, password)
        print(query)
        cursor.execute(query)

        # Fetch all rows from the result of the query
        rows = cursor.fetchone()

        # Print each row
        for row in rows:
            print(row)
        return rows
    except mysql.connector.Error as error:
        print(f"Error: {error}")
    finally:
        # Close the cursor and connection
        cursor.close()
        connection.close()



    
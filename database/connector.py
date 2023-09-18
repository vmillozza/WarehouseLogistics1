import mysql.connector as connector
import os

# Connect to MySQL database


def login(username, password):
    conn = connector.connect(host="localhost",
    username="root",
    password="",
    database="dbwarehouse")
    cursor = conn.cursor(buffered=True)

    # Ricerca dell'utente nel database
    cursor.execute('SELECT username,password FROM Utenti WHERE username =  %s AND password =  %s ', (username, password))
    row = cursor.fetchone()

    cursor.close()
    conn.close()
    return row

    



    
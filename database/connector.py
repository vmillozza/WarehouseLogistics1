import sqlite3 as sqlite3
import os

# Connect to MySQL database


def login(username, password):
   
    sqliteConnection = sqlite3.connect('./database/dbwarehouse.db')
    cursor = sqliteConnection.cursor()

    # Ricerca dell'utente nel database
    cursor.execute('SELECT username,password FROM Utenti WHERE username = ? AND password = ?', (username, password))

    row = cursor.fetchone()

    cursor.close()
    sqliteConnection.close()
    return row





    
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

def elenco_prodotti():
    conn = connector.connect(host="localhost",
    username="root",
    password="",
    database="dbwarehouse")
    cursor = conn.cursor(buffered=True)

    # Ricerca dei prodotti
    cursor.execute('SELECT nome_prodotto,codice,quantità,prezzo FROM prodotti ')
    rows = cursor.fetchall()
     # Print each row
    
    cursor.close()
    conn.close()
    return rows




    
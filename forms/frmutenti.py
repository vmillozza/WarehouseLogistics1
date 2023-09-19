import tkinter as tk
from tkinter import messagebox, simpledialog
import mysql.connector

# Connessione al database
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="dbwarehouse"
    )
def insert_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Utenti (username, password) VALUES (%s, %s)", (username, password))
    conn.commit()
    cursor.close()
    conn.close()

def update_user(userID, username, password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE Utenti SET username=%s, password=%s WHERE userID=%s", (username, password, userID))
    conn.commit()
    cursor.close()
    conn.close()


def add_user(username,password):
        insert_user(username, password)
def get_users():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Utenti")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return users
def main_window():

    '''
    listbox = tk.Listbox(root)
    listbox.pack(pady=20)

    btn_add = tk.Button(root, text="Aggiungi Utente", command=add_user)
    btn_add.pack()

    btn_edit = tk.Button(root, text="Modifica Utente", command=edit_user)
    btn_edit.pack()

    btn_delete = tk.Button(root, text="Cancella Utente", command=remove_user)
    btn_delete.pack()

    refresh_listbox()'''
    root = tk.Tk()
    root.title("Form di Registrazione")

    # Crea e posiziona le etichette e i campi di input
    username_label = tk.Label(root, text="Username:")
    username_label.pack(pady=10)

    username_entry = tk.Entry(root)
    username_entry.pack(pady=10)

    password_label = tk.Label(root, text="Password:")
    password_label.pack(pady=10)

    password_entry = tk.Entry(root, show="*")
    password_entry.pack(pady=10)

    # Crea e posiziona il pulsante di login
    reg_button = tk.Button(root, text="Registrati", command=add_user(username_entry.get(),password_entry.get()))
    reg_button.pack(pady=20)

    # Center the window on the screen
    window_width = 300
    window_height = 250

    # Get the screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate the x and y coordinates to center the window
    x = (screen_width / 2) - (window_width / 2)
    y = (screen_height / 2) - (window_height / 2)

    root.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}')

    root.mainloop()

  
        #refresh_listbox()

  




#main_window()


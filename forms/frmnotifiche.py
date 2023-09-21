import tkinter as tk
from tkinter import simpledialog, messagebox
import mysql.connector

# Connessione al database
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="dbwarehouse"
    )

# Funzioni CRUD
def insert_notification(message):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Notifiche (messaggio) VALUES (?)", (message,))
    conn.commit()
    cursor.close()
    conn.close()

def update_notification(id, new_message):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE Notifiche SET messaggio = ? WHERE notificaID = ?", (new_message, id))
    conn.commit()
    cursor.close()
    conn.close()

def delete_notification(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Notifiche WHERE notificaID = ?", (id,))
    conn.commit()
    cursor.close()
    conn.close()

def get_notifications():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Notifiche")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

# GUI
def main_window():
    root = tk.Tk()
    root.title("Gestione Notifiche")

    # Funzioni GUI
    def add():
        message = simpledialog.askstring("Inserisci", "Messaggio:")
        if message:
            insert_notification(message)
            refresh()

    def edit():
        selected = listbox.curselection()
        if selected:
            id, message, _ = listbox.get(selected[0]).split(' | ')
            new_message = simpledialog.askstring("Modifica", "Nuovo Messaggio:", initialvalue=message)
            if new_message:
                update_notification(id, new_message)
                refresh()

    def delete():
        selected = listbox.curselection()
        if selected:
            id, _, _ = listbox.get(selected[0]).split(' | ')
            delete_notification(id)
            refresh()

    def refresh():
        listbox.delete(0, tk.END)
        for row in get_notifications():
            listbox.insert(tk.END, f"{row[0]} | {row[1]} | {row[2]}")

    # Widgets
    listbox = tk.Listbox(root, width=100)
    listbox.pack(pady=20)

    btn_frame = tk.Frame(root)
    btn_frame.pack(pady=20)

    btn_add = tk.Button(btn_frame, text="Aggiungi", command=add)
    btn_add.grid(row=0, column=0, padx=10)

    btn_edit = tk.Button(btn_frame, text="Modifica", command=edit)
    btn_edit.grid(row=0, column=1, padx=10)

    btn_delete = tk.Button(btn_frame, text="Elimina", command=delete)
    btn_delete.grid(row=0, column=2, padx=10)

    btn_refresh = tk.Button(btn_frame, text="Aggiorna", command=refresh)
    btn_refresh.grid(row=0, column=3, padx=10)

    refresh()

    root.mainloop()

# Esegui la GUI
#main_window()

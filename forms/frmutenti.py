import tkinter as tk
from tkinter import messagebox, simpledialog
import sqlite3 as sqlite3
import login

# Connessione al database
def get_connection():
    # Connessione al database
        sqliteConnection = sqlite3.connect('./database/dbwarehouse.db')
        
        return sqliteConnection
    

def insert_user(username, password):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Utenti (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Si è verificato un errore: {e}")
        messagebox.showerror("Errore", f"Si è verificato un errore: {e}")

def add_user(username, password,root):
    vuoti = username.strip() == "" or password.strip() == ""
    if vuoti:
        messagebox.showerror("Errore", "Username e password non possono essere vuoti")
        return
    insert_user(username, password)
    messagebox.showinfo("Info", "Username e password ok")
    root.destroy()
    login.authenticate()

def main_window():
    root = tk.Tk()
    root.title("Form di Registrazione")

    main_frame = tk.Frame(root, padx=20, pady=20)
    main_frame.pack(padx=10, pady=10)

    # Crea e posiziona le etichette e i campi di input
    username_label = tk.Label(main_frame, text="Username:")
    username_label.grid(row=0, column=0, sticky="w", pady=5)

    username_entry = tk.Entry(main_frame)
    username_entry.grid(row=0, column=1, pady=5)

    password_label = tk.Label(main_frame, text="Password:")
    password_label.grid(row=1, column=0, sticky="w", pady=5)

    password_entry = tk.Entry(main_frame, show="*")
    password_entry.grid(row=1, column=1, pady=5)

    # Crea e posiziona il pulsante di registrazione
    reg_button = tk.Button(main_frame, text="Registrati", bg='#4CAF50', fg='white',width=10 ,command=lambda: add_user(username_entry.get(), password_entry.get(),root))
    reg_button.grid(row=2, column=0, columnspan=2, pady=20)

    window_width = 300
    window_height = 250

   
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width / 2) - (window_width / 2)
    y = (screen_height / 2) - (window_height / 2)

    root.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}')

    root.mainloop()

#main_window()

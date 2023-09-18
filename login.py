import tkinter as tk
from tkinter import messagebox
from database import connector as connector

def authenticate():
    
    rows = connector.fetch_data_from_utente(username_entry.get(),password_entry.get())
    
    # Verifica se la coppia esiste nella lista
    if len(rows)==1:
        print("La coppia è presente nella lista!")
    else:
        print("La coppia non è presente nella lista.")

# Crea la finestra principale

root = tk.Tk()
root.title("Form di Autenticazione")

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
login_button = tk.Button(root, text="Login", command=authenticate)
login_button.pack(pady=20)

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

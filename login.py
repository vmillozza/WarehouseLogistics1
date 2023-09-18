import tkinter as tk
from tkinter import messagebox
from database import connector as connector

def authenticate():
    if username_entry.get() == "admin" and password_entry.get() == "password":
        messagebox.showinfo("Successo", "Accesso effettuato con successo!")
    else:
        messagebox.showerror("Errore", "Username o password errati!")

# Crea la finestra principale
if(connector.doconnect()):
    messagebox.showinfo("Successo", "Caricamento db effettuato con successo!")
else:
    messagebox.showerror("Errore", "Caricamento db fallito!")
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

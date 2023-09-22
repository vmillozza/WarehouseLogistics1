import tkinter as tk
from tkinter import messagebox, font
from database import connector as connector
from forms import frmprodotti, frmutenti

def display_products():
    frmprodotti.main_window()

def close_form():
    root.destroy()

def registrati():
    close_form()
    frmutenti.main_window()
    
    




def authenticate():
    try:
        vuoti = username_entry.get().strip() == "" or password_entry.get().strip() == ""

        if vuoti:
            messagebox.showerror("Errore", "Username e password non possono essere vuoti")
            username_entry.focus_get()
            return
        
        row = connector.login(username_entry.get(), password_entry.get())

        if row is not None:
            print("Login eseguito con successo")
            close_form()
            frmprodotti.ProdottiApp()
        else:
            print("Login non eseguito con successo")
            messagebox.showerror("Errore", "Login non eseguito con successo")
    except Exception as e:
        print(f"Si è verificato un errore: {e}")
        messagebox.showerror("Errore", f"Si è verificato un errore: {e}")

root = tk.Tk()
root.title("Form di Autenticazione")
root.configure(bg='#f2f2f2')

# Font personalizzati
label_font = font.Font(size=12, weight='bold')
entry_font = font.Font(size=10)
button_font = font.Font(size=10, weight='bold')

# Frame centrale
frame = tk.Frame(root, bg='#f2f2f2')
frame.pack(pady=40, padx=40)

# Etichette, campi di input e pulsanti
username_label = tk.Label(frame, text="Username:", font=label_font, bg='#f2f2f2')
username_label.grid(row=0, column=0, sticky='w', pady=10)

username_entry = tk.Entry(frame, font=entry_font)
username_entry.insert(0, "lallo")
username_entry.grid(row=1, column=0, pady=5, padx=20, sticky='ew')

password_label = tk.Label(frame, text="Password:", font=label_font, bg='#f2f2f2')
password_label.grid(row=2, column=0, sticky='w', pady=10)

password_entry = tk.Entry(frame, show="*", font=entry_font)
password_entry.insert(0, "password")
password_entry.grid(row=3, column=0, pady=5, padx=20, sticky='ew')

login_button = tk.Button(frame, text="Login", command=authenticate, font=button_font, bg='#4CAF50', fg='white')
login_button.grid(row=4, column=0, pady=20, padx=20, sticky='ew')

reg_button = tk.Button(frame, text="Registrati", command=registrati, font=button_font, bg='#FFC107')
reg_button.grid(row=5, column=0, pady=5, padx=20, sticky='ew')

window_width = 350
window_height = 400

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (window_width / 2)
y = (screen_height / 2) - (window_height / 2)

root.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}')

root.mainloop()

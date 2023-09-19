import tkinter as tk
from tkinter import simpledialog, messagebox
from forms import frmnotifiche,frmprodotti
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
def insert_order(prodottoID, quantità_ordinata, codice_spedizione):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Ordini (prodottoID, quantità_ordinata, codice_spedizione) VALUES (%s, %s, %s)", (prodottoID, quantità_ordinata, codice_spedizione))
    conn.commit()
    cursor.close()
    conn.close()

def update_order(ordineID, prodottoID, quantità_ordinata, codice_spedizione):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE Ordini SET prodottoID=%s, quantità_ordinata=%s, codice_spedizione=%s WHERE ordineID=%s", (prodottoID, quantità_ordinata, codice_spedizione, ordineID))
    conn.commit()
    cursor.close()
    conn.close()

def delete_order(ordineID):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Ordini WHERE ordineID=%s", (ordineID,))
    conn.commit()
    cursor.close()
    conn.close()

def get_orders():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Ordini")
    orders = cursor.fetchall()
    cursor.close()
    conn.close()
    return orders

# GUI
def main_window():
    root = tk.Tk()
    root.title("Gestione Ordini")

    # Funzioni per i pulsanti
    def add_order():
        prodottoID = simpledialog.askinteger("Inserisci Ordine", "Inserisci ID Prodotto:")
        quantità_ordinata = simpledialog.askinteger("Inserisci Ordine", "Inserisci Quantità Ordinata:")
        codice_spedizione = simpledialog.askstring("Inserisci Ordine", "Inserisci Codice Spedizione:")
        insert_order(prodottoID, quantità_ordinata, codice_spedizione)
        #- Quando un prodotto viene ordinato.
        frmnotifiche.insert_notification('Oradinato un nuovo rodotto %s  ',prodottoID)
        '''
        - Gestione Ordini: Quando un ordine viene effettuato, il sistema deve:
        - Ridurre automaticamente la quantità del prodotto in magazzino.
         
        - Generare un codice di spedizione casuale se il prodotto è disponibile.
        - Segnare la riga in rosso se il prodotto non è disponibile.
        '''
        frmprodotti.decrement_product_quantity(prodottoID)
        
        show_orders()

    def edit_order():
        ordineID = simpledialog.askinteger("Modifica Ordine", "Inserisci ID Ordine da modificare:")
        prodottoID = simpledialog.askinteger("Modifica Ordine", "Inserisci nuovo ID Prodotto:")
        quantità_ordinata = simpledialog.askinteger("Modifica Ordine", "Inserisci nuova Quantità Ordinata:")
        codice_spedizione = simpledialog.askstring("Modifica Ordine", "Inserisci nuovo Codice Spedizione:")
        update_order(ordineID, prodottoID, quantità_ordinata, codice_spedizione)
        show_orders()

    def remove_order():
        ordineID = simpledialog.askinteger("Rimuovi Ordine", "Inserisci ID Ordine da rimuovere:")
        delete_order(ordineID)
        show_orders()

    def show_orders():
        for widget in root.winfo_children():
            widget.destroy()
        orders = get_orders()
        i = 0  # Inizializza i a 0
        for i, order in enumerate(orders):
            for j, field in enumerate(order):
                e = tk.Entry(root)
                e.grid(row=i, column=j)
                e.insert(tk.END, field)
        tk.Button(root, text="Aggiungi Ordine", command=add_order).grid(row=i+1, column=0)
        tk.Button(root, text="Modifica Ordine", command=edit_order).grid(row=i+1, column=1)
        tk.Button(root, text="Rimuovi Ordine", command=remove_order).grid(row=i+1, column=2)

    show_orders()
    # Center the window on the screen
    window_width = 500
    window_height = 350

    # Get the screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate the x and y coordinates to center the window
    x = (screen_width / 2) - (window_width / 2)
    y = (screen_height / 2) - (window_height / 2)

    root.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}')
    root.mainloop()

# Esegui la GUI
main_window()

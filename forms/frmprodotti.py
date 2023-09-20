import tkinter as tk
from tkinter import messagebox, simpledialog
from forms import frmnotifiche
import mysql.connector

# Connessione al database
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="dbwarehouse"
    )
def insert_product(nome, codice, quantita, prezzo):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Prodotti (nome_prodotto, codice, quantità, prezzo) VALUES (%s, %s, %s, %s)", (nome, codice, quantita, prezzo))
    #- Quando un nuovo prodotto entra in magazzino.
    frmnotifiche.insert_notification('Inserito un nuovo prodotto %s %s' % (nome, codice))
    conn.commit()
    cursor.close()
    conn.close()

def update_product(prodottoID, nome, codice, quantita, prezzo):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE Prodotti SET nome_prodotto=%s, codice=%s, quantità=%s, prezzo=%s WHERE prodottoID=%s", (nome, codice, quantita, prezzo, prodottoID))
    conn.commit()
    cursor.close()
    conn.close()
def decrement_product_quantity(prodottoID):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE Prodotti SET quantità=quantità-1 where quantità > 0",  prodottoID)
    conn.commit()
    cursor.close()
    conn.close()
def delete_product(prodottoID,quantita):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE Prodotti SET quantità=%s WHERE prodottoID=%s", (quantita, prodottoID))

    conn.commit()
    cursor.close()
    conn.close()

def get_products():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Prodotti")
    products = cursor.fetchall()
    cursor.close()
    conn.close()
    return products

def get_products_with_quantity(q):
    conn = get_connection()
    cursor = conn.cursor()
    print("SELECT nome_prodotto FROM Prodotti where quantità=%s",(q,))
    cursor.execute("SELECT nome_prodotto FROM Prodotti where quantità=%s",(q,))
    products = cursor.fetchall()
    cursor.close()
    conn.close()
    return products
def main_window():
    root = tk.Tk()
    root.title("Gestione Prodotti")
    
    def refresh_listbox():
        products = get_products()
        listbox.delete(0, tk.END)
        for product in products:
            listbox.insert(tk.END, f"{product[0]} - {product[1]} -{product[2]}-{product[3]}-{product[4]}")

    def add_product():
        nome = simpledialog.askstring("Inserimento", "Nome Prodotto:")
        codice = simpledialog.askstring("Inserimento", "Codice:")
        quantita = simpledialog.askinteger("Inserimento", "Quantità:")
        prezzo = simpledialog.askfloat("Inserimento", "Prezzo:")
        insert_product(nome, codice, quantita, prezzo)
        refresh_listbox()

    def edit_product():
        selected = listbox.curselection()
        if not selected:
            return
        prodottoID = int(listbox.get(selected).split(" - ")[0])
        nome = simpledialog.askstring("Modifica", "Nome Prodotto:")
        codice = simpledialog.askstring("Modifica", "Codice:")
        quantita = simpledialog.askinteger("Modifica", "Quantità:")
        prezzo = simpledialog.askfloat("Modifica", "Prezzo:")
        update_product(prodottoID, nome, codice, quantita, prezzo)
        refresh_listbox()

    def remove_product():
        selected = listbox.curselection()
        if not selected:
            return
        prodottoID = int(listbox.get(selected).split(" - ")[0])
        delete_product(prodottoID,None)
        refresh_listbox()
    
    prodotti_quantita_uno = len(get_products_with_quantity(1)) >0
    prodotti_quantita_zero =len(get_products_with_quantity(0)) >0

    if(prodotti_quantita_uno):
        frmnotifiche.insert_notification('I seguenti prodotti stanno per esaurirsi')
    if(prodotti_quantita_zero):
        frmnotifiche.insert_notification('I seguenti prodotti non sono più disponibili')
    
    listbox = tk.Listbox(root, width=100)
    listbox.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

    btn_add = tk.Button(root, text="Aggiungi", command=add_product)
    btn_add.grid(row=1, column=0, padx=10, pady=10)

    btn_edit = tk.Button(root, text="Modifica", command=edit_product)
    btn_edit.grid(row=1, column=1, padx=10, pady=10)

    btn_delete = tk.Button(root, text="Cancella", command=remove_product)
    btn_delete.grid(row=1, column=2, padx=10, pady=10)

    refresh_listbox()

    # Center the window on the screen
    window_width = 600  # Aumentato per adattarsi meglio ai contenuti
    window_height = 450

    # Get the screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate the x and y coordinates to center the window
    x = (screen_width / 2) - (window_width / 2)
    y = (screen_height / 2) - (window_height / 2)

    root.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}')

    root.mainloop()
    #main_window()



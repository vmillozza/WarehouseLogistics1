import tkinter as tk
from tkinter import END, Entry, Listbox


from database import connector as connector

def display_products():
    # Lista di prodotti (puoi sostituirla con i dati provenienti da un database o da un'altra fonte)
    products = connector.elenco_prodotti()
    for row in products:
            print(row)
    

    # Crea una finestra principale
    root = tk.Tk()
    root.title("Elenco Prodotti")
    e=tk.Label(root,width=10,text='Nome',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=0)
    e=tk.Label(root,width=10,text='Codice',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=1)
    e=tk.Label(root,width=10,text='Quantità',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=2)
    e=tk.Label(root,width=10,text='Prezzo',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=3)
    
    i=1 
    for product in products: 
        for j in range(len(product)):
            e = Entry(root, width=50, fg='blue') 
            e.grid(row=i, column=j) 
            e.insert(END, product[j])
        i=i+1
    
    # Avvia il loop principale di tkinter
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 900
    window_height = 500
    # Calculate the x and y coordinates to center the window
    x = (screen_width / 2) - (window_width / 2)
    y = (screen_height / 2) - (window_height / 2)

    root.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}')
    root.mainloop()

# Esegui la funzione per visualizzare la form


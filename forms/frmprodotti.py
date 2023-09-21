from tkcalendar import Calendar, DateEntry
import tkinter as tk
import tkinter.messagebox as mb
import tkinter.ttk as ttk
import sqlite3 as sqlite3

# Connessione al database
sqliteConnection = sqlite3.connect('./database/dbwarehouse.db')
cursor = sqliteConnection.cursor()


class ProdottiApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestione Prodotti")
        self.geometry("800x650+351+174")

        # Etichette e campi di input
        self.lblTitle = tk.Label(self, text="Gestione Prodotti", font=("Helvetica", 16), bg="yellow", fg="green")
        self.lblNomeProdotto = tk.Label(self, text="Nome Prodotto:", font=("Helvetica", 10), bg="blue", fg="yellow")
        self.lblCodice = tk.Label(self, text="Codice:", font=("Helvetica", 10), bg="blue", fg="yellow")
        self.lblQuantita = tk.Label(self, text="Quantità:", font=("Helvetica", 10), bg="blue", fg="yellow")
        self.lblPrezzo = tk.Label(self, text="Prezzo:", font=("Helvetica", 10), bg="blue", fg="yellow")

        self.entNomeProdotto = tk.Entry(self)
        self.entCodice = tk.Entry(self)
        self.entQuantita = tk.Entry(self)
        self.entPrezzo = tk.Entry(self)

        # Posizionamento degli elementi
        self.lblTitle.pack(pady=20)
        self.lblNomeProdotto.pack(pady=5)
        self.entNomeProdotto.pack(pady=5)
        self.lblCodice.pack(pady=5)
        self.entCodice.pack(pady=5)
        self.lblQuantita.pack(pady=5)
        self.entQuantita.pack(pady=5)
        self.lblPrezzo.pack(pady=5)
        self.entPrezzo.pack(pady=5)

        # Bottoni
        self.btn_register = tk.Button(self, text="Registra", command=self.register_prodotto)
        self.btn_register.pack(pady=20)

        # Treeview per mostrare i prodotti
        self.tvProdotti = ttk.Treeview(self, columns=('Nome Prodotto', 'Codice', 'Quantità', 'Prezzo'))
        self.tvProdotti.heading('Nome Prodotto', text='Nome Prodotto')
        self.tvProdotti.heading('Codice', text='Codice')
        self.tvProdotti.heading('Quantità', text='Quantità')
        self.tvProdotti.heading('Prezzo', text='Prezzo')
        self.tvProdotti.pack(pady=20)

        self.load_prodotti_data()

    def register_prodotto(self):
        nome_prodotto = self.entNomeProdotto.get()
        codice = self.entCodice.get()
        quantita = self.entQuantita.get()
        prezzo = self.entPrezzo.get()

        try:
            query = "INSERT INTO Prodotti (nome_prodotto, codice, quantità, prezzo) VALUES (?, ?, ?, ?)"
            cursor.execute(query, (nome_prodotto, codice, quantita, prezzo))
            sqliteConnection.commit()
            mb.showinfo('Informazione', "Prodotto registrato con successo!")
            self.load_prodotti_data()
        except sqlite3.Connection.Error as err:
            print(err)
            mb.showinfo('Informazione', "Errore nell'inserimento del prodotto!")
            sqliteConnection.rollback()

    def load_prodotti_data(self):
        self.tvProdotti.delete(*self.tvProdotti.get_children())
        query = "SELECT nome_prodotto, codice, quantità, prezzo FROM Prodotti"
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            self.tvProdotti.insert("", 'end', values=row)

if __name__ == "__main__":
    app = ProdottiApp()
    app.mainloop()

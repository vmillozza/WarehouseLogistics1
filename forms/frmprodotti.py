from tkcalendar import Calendar, DateEntry
import tkinter as tk
import tkinter.messagebox as mb
import tkinter.ttk as ttk
import sqlite3 as sqlite3

from forms import frmordini,frmnotifiche

# Connessione al database
sqliteConnection = sqlite3.connect('./database/dbwarehouse.db')
cursor = sqliteConnection.cursor()


class ProdottiApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestione Prodotti")
        self.geometry("1200x650+351+174")

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
        #self.entSearch = tk.Entry(self)
        self.btn_gest_ordini = tk.Button(self, text="Ordini", font=("Helvetica", 11), bg="yellow", fg="blue",command=self.GestOrdini)
        
       
        # Bottoni
        self.btn_register = tk.Button(self, text="Registra", command=self.register_prodotto)
        self.btn_register.pack(pady=20)
      
        self.btn_delete = tk.Button(self, text="Delete", font=("Helvetica", 11), bg="yellow", fg="blue",
                                    command=self.delete_product_data)
        self.btn_delete.pack()
        self.btn_update = tk.Button(self,text="Update",font=("Helvetica",11),bg="yellow", fg="blue",command=self.update_prodotti_data)
        self.btn_update.pack()
        # Treeview per mostrare i prodotti
        self.btn_gest_ordini.pack()
        
        self.tvProdotti = ttk.Treeview(self, columns=('Id','Nome Prodotto', 'Codice', 'Quantità', 'Prezzo'))
        self.tvProdotti.heading('Id', text='Id')
        self.tvProdotti.heading('Nome Prodotto', text='Nome Prodotto')
        self.tvProdotti.heading('Codice', text='Codice')
        self.tvProdotti.heading('Quantità', text='Quantità')
        self.tvProdotti.heading('Prezzo', text='Prezzo')
        self.tvProdotti.pack(pady=20)
        self.tvProdotti.bind("<<TreeviewSelect>>", self.show_selected_record)
        self.load_prodotti_data()
    def update_prodotti_data(self):
    
        nome_prodotto = self.entNomeProdotto.get()  # Assumo che tu stia cercando di ottenere il valore da un widget Entry
        codice = self.entCodice.get()
        quantita = self.entQuantita.get()
        prezzo = self.entPrezzo.get()
        for selection in self.tvProdotti.selection():
            item = self.tvProdotti.item(selection)
        Id = item["values"][0]
        # Preparazione della query
        Update = "UPDATE Prodotti SET nome_prodotto=?, codice=?, quantità=?, prezzo=? WHERE prodottoID=?"

        # Esecuzione della query con parametri
        cursor.execute(Update, (nome_prodotto, codice, quantita, prezzo, Id))  # Assumo che prodottoID sia definito altrove nel tuo codice

        sqliteConnection.commit()
        mb.showinfo("Info", "Aggiornato con successo")
        self.load_prodotti_data()
    def close_form(self):
        self.destroy()
    
    def GestOrdini(self):
        if(len(self.tvProdotti.selection())!=0):
            for selection in self.tvProdotti.selection():
                item = self.tvProdotti.item(selection)
                Id = item["values"][0]
                #Nome = item["values"][1]
        else:
           Id=None
        self.close_form()
        frmordini.OrdiniApp(IdProdotto=Id)
    
    def register_prodotto(self):
        if(self.entNomeProdotto.get().strip()!="") :
           nome_prodotto = self.entNomeProdotto.get()
        else:
         mb.showerror("Errore", "Si è verificato un errore:Nome prodotto non può essere vuoto")
         return
        
        if(self.entCodice.get().strip()!="") :
           codice = self.entCodice.get() 
        else:
           mb.showerror("Errore", "Si è verificato un errore:Codice non può essere vuoto")
           return
        
        if(self.entQuantita.get().strip()!="") :
           quantita = self.entQuantita.get() 
        else:
           mb.showerror("Errore", "Si è verificato un errore:Quantita non può essere vuoto")
           return
        
        if(self.entPrezzo.get().strip()!="") :
           prezzo = self.entPrezzo.get() 
        else:
           mb.showerror("Errore", "Si è verificato un errore:Prezzo non può essere vuoto")
           return
        try:
            query = "INSERT INTO Prodotti (nome_prodotto, codice, quantità, prezzo) VALUES (?, ?, ?, ?)"
            cursor.execute(query, (nome_prodotto, codice, quantita, prezzo))
            sqliteConnection.commit()
            mb.showinfo('Informazione', "Prodotto registrato con successo!")
            self.load_prodotti_data()
            frmnotifiche.insert_notification('Inserito un nuovo prodotto ' + codice)
           
        except sqlite3.Error as err:
            print(err)
            cursor.close()
            sqliteConnection.close()
            mb.showinfo('Informazione', "Errore nell'inserimento del prodotto!")
            sqliteConnection.rollback()
 

    def delete_product_data(self):
      MsgBox = mb.askquestion('Cancella record', 'Sei sicuro di volerlo cancellare?', icon='warning')
      if MsgBox == 'yes':
          for selection in self.tvProdotti.selection():
            item = self.tvProdotti.item(selection)
          Id = item["values"][0]
          query = "DELETE FROM Prodotti WHERE prodottoID=?"
          cursor.execute(query, (Id,))
          sqliteConnection.commit()
          mb.showinfo("Information", "Record cancellato")
          self.clear_form()
          self.load_prodotti_data()
          
    def load_prodotti_data(self):
        self.tvProdotti.delete(*self.tvProdotti.get_children())
        query = "SELECT prodottoID,nome_prodotto, codice, quantità, prezzo FROM Prodotti"
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            self.tvProdotti.insert("", 'end', values=row)
    def show_selected_record(self,event):
        self.clear_form()
        for selection in self.tvProdotti.selection():
            item = self.tvProdotti.item(selection)
        Id,nome_prodotto, codice, quantita, prezzo = item["values"][0:7]
        self.entNomeProdotto.insert(0, nome_prodotto)
        self.entCodice.insert(0, codice)
        self.entQuantita.insert(0, quantita)
        self.entPrezzo .insert(0, prezzo)
     
        return Id
    
    def clear_form(self):
        self.entNomeProdotto.delete(0, tk.END)
        self.entCodice.delete(0, tk.END)
        self.entQuantita.delete(0, tk.END)
        self.entPrezzo.delete(0, tk.END)
    def exit(self):
      MsgBox = mb.askquestion('Exit Application', 'Sei sicuro di voler uscire?', icon='warning')
      if MsgBox == 'yes':
        self.destroy()
if __name__ == "__main__":
    app = ProdottiApp()
    app.mainloop()

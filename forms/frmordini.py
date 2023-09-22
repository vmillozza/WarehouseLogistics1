from tkcalendar import Calendar, DateEntry
import tkinter as tk
import tkinter.messagebox as mb
import tkinter.ttk as ttk
import sqlite3 as sqlite3

from forms import frmnotifiche
# Connessione al database
sqliteConnection = sqlite3.connect('./database/dbwarehouse.db')
cursor = sqliteConnection.cursor()


class OrdiniApp(tk.Tk):

    def __init__(self,IdProdotto):
        super().__init__()
        self.title("Gestione Ordini")
        self.geometry("1200x650+351+174")

        def on_combobox_select(event):
                selected_value = self.combobox.get()
                print(f"Selected product: {selected_value}")
        # Etichette e campi di input
        self.lblTitle = tk.Label(self, text="Gestione Ordini", font=("Helvetica", 16), bg="yellow", fg="green")
        # Etichette e campi di input
       
        self.lblProdottoId = tk.Label(self, text="Prodotto Id:", font=("Helvetica", 10), bg="blue", fg="yellow")
        self.lblCodice = tk.Label(self, text="Codice:", font=("Helvetica", 10), bg="blue", fg="yellow")
        self.lblQuantita = tk.Label(self, text="Quantità:", font=("Helvetica", 10), bg="blue", fg="yellow")
       

        #self.entProdottoId = tk.Entry(self)
        # Crea un Combobox
        # Crea un Combobox per i prodotti
        self.combobox = ttk.Combobox(self, values=("Prodotto 1", "Prodotto 2", "Prodotto 3"))
        
        self.combobox.set("Seleziona un prodotto")
        self.combobox.bind("<<ComboboxSelected>>", on_combobox_select)
        self.load_combobox_values()

        self.entCodice = tk.Entry(self)
        self.entQuantita = tk.Entry(self)
        

        # Posizionamento degli elementi
        self.lblTitle.pack(pady=20)
        self.lblProdottoId.pack(pady=5)
        self.combobox.pack(pady=5)  # Posiziona il Combobox
        self.lblCodice.pack(pady=5)
        self.entCodice.pack(pady=5)
        self.lblQuantita.pack(pady=5)
        self.entQuantita.pack(pady=5)
        
        self.entSearch = tk.Entry(self)
        self.btn_search = tk.Button(self, text="Search", font=("Helvetica", 11), bg="yellow", fg="blue",command=None)
        
       
        # Bottoni
        self.btn_register = tk.Button(self, text="Registra", command=self.register_ordine)
        self.btn_register.pack(pady=20)
      
        self.btn_delete = tk.Button(self, text="Delete", font=("Helvetica", 11), bg="yellow", fg="blue",
                                    command=self.delete_ordine_data)
        self.btn_delete.pack()
        self.btn_update = tk.Button(self,text="Update",font=("Helvetica",11),bg="yellow", fg="blue",command=self.update_ordini_data)
        self.btn_update.pack()
        # Treeview per mostrare i prodotti
        
        self.tvOrdini = ttk.Treeview(self, columns=('Id','Prodotto Id','Quantità','Codice'))
        self.tvOrdini.heading('Id', text='Id')
        self.tvOrdini.heading('Prodotto Id', text='Prodotto Id')
        
        self.tvOrdini.heading('Quantità', text='Quantità')
        self.tvOrdini.heading('Codice', text='Codice')
        self.tvOrdini.pack(pady=20)
        self.tvOrdini.bind("<<TreeviewSelect>>", self.show_selected_record)
        if(IdProdotto==None):
            self.load_ordini_data()
        else:
            self.load_ordini_data_by_IdProdotto(IdProdotto)
    
    def load_combobox_values(self):
        # Esegui una query sul database per ottenere i nomi dei prodotti (o qualsiasi altro valore desideri)
        cursor.execute("SELECT prodottoID,nome_prodotto FROM Prodotti")
        products = cursor.fetchall()

        # Estrai i valori dalla tupla e popola il Combobox

        self.combobox['values']  = products
        
    def update_ordini_data(self):
    
        prodotto_id = self.combobox.get().split(" ")[0]  # Assumo che tu stia cercando di ottenere il valore da un widget Entry
        codice = self.entCodice.get()
        quantita = self.entQuantita.get()
        for selection in self.tvOrdini.selection():
            item = self.tvOrdini.item(selection)
        Id = item["values"][0]
        # Preparazione della query
        Update = "UPDATE Ordini SET prodottoID=?, codice=?, quantità_ordinata=?, codice_spedizione=? WHERE ordineID=?"

        # Esecuzione della query con parametri
        cursor.execute(Update, (prodotto_id, codice, quantita, Id))  # Assumo che prodottoID sia definito altrove nel tuo codice

        sqliteConnection.commit()
        mb.showinfo("Info", "Aggiornato con successo")
        self.load_ordini_data()

    def register_ordine(self):
        if(self.combobox.get().split(" ")[0]!="" or self.combobox.get()!="Seleziona un prodotto") :
           prodotto_id = self.combobox.get().split(" ")[0]
        else:
         mb.showerror("Errore", "Si è verificato un errore:id prodotto non può essere vuoto")
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
      
        try:
            sqliteConnection = sqlite3.connect('./database/dbwarehouse.db')
            cursor = sqliteConnection.cursor()
            query = "INSERT INTO Ordini (prodottoID,quantità_ordinata ,codice_spedizione) VALUES (?, ?, ?)"
            cursor.execute(query, (prodotto_id, quantita,codice))
            sqliteConnection.commit()
            mb.showinfo('Informazione', "Ordine registrato con successo!")
            self.load_ordini_data()
            frmnotifiche.insert_notification('Inserito un nuovo ordine ' + codice)

        except sqlite3.Error as err:
            print(err)
            cursor.close()
            sqliteConnection.close()
            mb.showinfo('Informazione', "Errore nell'inserimento dell 'ordine!")
            sqliteConnection.rollback()
 

    def delete_ordine_data(self):
      MsgBox = mb.askquestion('Cancella record', 'Sei sicuro di volerlo cancellare?', icon='warning')
      if MsgBox == 'yes':
          for selection in self.tvOrdini.selection():
            item = self.tvOrdini.item(selection)
          Id = item["values"][0]
          query = "DELETE FROM Ordini WHERE ordineID=?"
          cursor.execute(query, (Id,))
          sqliteConnection.commit()
          mb.showinfo("Information", "Record cancellato")
          self.clear_form()
          self.load_prodotti_data()
          
    def load_ordini_data(self):
        self.tvOrdini.delete(*self.tvOrdini.get_children())
        query = "SELECT ordineID,prodottoID,quantità_ordinata, codice_spedizione FROM Ordini"
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            self.tvOrdini.insert("", 'end', values=row)
    def load_ordini_data_by_IdProdotto(self,IdProdotto):
        self.tvOrdini.delete(*self.tvOrdini.get_children())
        query = "SELECT ordineID,prodottoID,quantità_ordinata, codice_spedizione FROM Ordini where prodottoID = "+str(IdProdotto)
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            self.tvOrdini.insert("", 'end', values=row)
    def show_selected_record(self,event):
        self.clear_form()
        for selection in self.tvOrdini.selection():
            item = self.tvOrdini.item(selection)
        Id,prodottoId, quantita,codice = item["values"][0:7]
        #self.entProdottoId.insert(0, prodottoId)
        self.entCodice.insert(0, codice)
        self.entQuantita.insert(0, quantita)
        
     
        return Id
    
    def clear_form(self):
        #self.entProdottoId.delete(0, tk.END)
        self.entCodice.delete(0, tk.END)
        self.entQuantita.delete(0, tk.END)
        
    def exit(self):
      MsgBox = mb.askquestion('Exit Application', 'Sei sicuro di voler uscire?', icon='warning')
      if MsgBox == 'yes':
        self.destroy()
if __name__ == "__main__":
    app = OrdiniApp()
    app.mainloop()

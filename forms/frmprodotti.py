from tkcalendar import Calendar, DateEntry
import tkinter as tk
import tkinter.messagebox as mb
import tkinter.ttk as ttk

## Connecting to the database

## importing 'mysql.connector' for connection to mysql database
import mysql.connector

## connecting to the database using 'connect()' method
## it takes 3 required parameters 'host', 'user', 'password'
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="")
# creating database_cursor to perform SQL operation
db_cursor = db_connection.cursor(buffered=True)  # "buffered=True".makes db_cursor.row_count return actual number of records selected otherwise would return -1


class ProductApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Product Management System")
        self.geometry("800x650+351+174")
        self.lblTitle = tk.Label(self, text="Product Management System", font=("Helvetica", 16), bg="yellow", fg="green")
        self.lblFName = tk.Label(self, text="Nome Prodotto:", font=("Helvetica", 10), bg="blue", fg="yellow")
        self.lblCodice = tk.Label(self, text="Codice:", font=("Helvetica", 10), bg="blue", fg="yellow")
        self.lblQuantita = tk.Label(self, text="Quantità:", font=("Helvetica", 10), bg="blue", fg="yellow")
        self.lblPrezzo = tk.Label(self, text="Prezzo:", font=("Helvetica", 10), bg="blue", fg="yellow")
        

        self.entFName = tk.Entry(self)
        self.entLCode = tk.Entry(self)
        self.entQuant = tk.Entry(self)
        self.entPrice = tk.Entry(self)
        
       
        self.entSearch = tk.Entry(self)


        self.btn_register = tk.Button(self, text="Registra", font=("Helvetica", 11), bg="yellow", fg="blue",
                                      command=self.register_product)
        self.btn_update = tk.Button(self,text="Update",font=("Helvetica",11),bg="yellow", fg="blue",command=self.update_product)
        self.btn_delete = tk.Button(self, text="Delete", font=("Helvetica", 11), bg="yellow", fg="blue",
                                    command=self.delete_product)
        self.btn_clear = tk.Button(self, text="Clear", font=("Helvetica", 11), bg="yellow", fg="blue",
                                    command=self.clear_form)
        self.btn_show_all = tk.Button(self, text="Show All", font=("Helvetica", 11), bg="yellow", fg="blue",
                                   command=self.load_product_data)
        self.btn_search = tk.Button(self, text="Search", font=("Helvetica", 11), bg="yellow", fg="blue",
                                   command=self.show_search_record)
        self.btn_exit = tk.Button(self, text="Exit", font=("Helvetica", 16), bg="yellow", fg="blue",command=self.exit)

        columns = ("#1", "#2", "#3", "#4", "#5")
        self.tvProduct= ttk.Treeview(self,show="headings",height="5", columns=columns)
        self.tvProduct.heading('#1', text='No', anchor='center')
        self.tvProduct.column('#1', width=60, anchor='center', stretch=False)
        self.tvProduct.heading('#2', text='Name', anchor='center')
        self.tvProduct.column('#2', width=10, anchor='center', stretch=True)
        self.tvProduct.heading('#3', text='Codice', anchor='center')
        self.tvProduct.column('#3',width=10, anchor='center', stretch=True)
        self.tvProduct.heading('#4', text='Quantità', anchor='center')
        self.tvProduct.column('#4',width=10, anchor='center', stretch=True)
        self.tvProduct.heading('#5', text='Prezzo', anchor='center')
        self.tvProduct.column('#5',width=10, anchor='center', stretch=True)
      

        #Scroll bars are set up below considering placement position(x&y) ,height and width of treeview widget
        vsb= ttk.Scrollbar(self, orient=tk.VERTICAL,command=self.tvProduct.yview)
        vsb.place(x=40 + 640 + 1, y=310, height=180 + 20)
        self.tvProduct.configure(yscroll=vsb.set)
        hsb = ttk.Scrollbar(self, orient=tk.HORIZONTAL, command=self.tvProduct.xview)
        hsb.place(x=40 , y=310+200+1, width=620 + 20)
        self.tvProduct.configure(xscroll=hsb.set)
        self.tvProduct.bind("<<TreeviewSelect>>", self.show_selected_record)

        self.lblFName.place(x=280, y=30,  height=27, width=300)
        self.lblCodice.place(x=175, y=70,  height=23, width=100)
        self.lblQuantita.place(x=175, y=100,  height=23, width=100)
        self.lblPrezzo.place(x=171, y=129,  height=23, width=104)
       

        self.entFName.place(x=277, y=72, height=21, width=186)
        self.entLCode.place(x=277, y=100, height=21, width=186)
        self.entPrice.place(x=277, y=129, height=21, width=186)
        self.entQuant.place(x=277, y=158, height=21, width=186)
       

        self.entSearch.place(x=310, y=560, height=21, width=186)
        self.btn_register.place(x=290, y=245, height=25, width=76)
        self.btn_update.place(x=370, y=245, height=25, width=76)
        self.btn_delete.place(x=460, y=245, height=25, width=76)
        self.btn_clear.place(x=548, y=245, height=25, width=76)
        self.btn_show_all.place(x=630, y=245, height=25, width=76)
        self.btn_search.place(x=498, y=558, height=26, width=60)
        self.btn_exit.place(x=320, y=610,  height=31, width=60)
        self.tvProduct.place(x=40, y=310, height=200, width=640)
        
        self.load_product_data()

    def clear_form(self):
      self.entFName.delete(0, tk.END)
      self.entLName.delete(0, tk.END)
      self.entContact.delete(0, tk.END)
      self.entCity.delete(0, tk.END)
      self.entState.delete(0, tk.END)
      self.calDOB.delete(0, tk.END)



    def exit(self):
      MsgBox = mb.askquestion('Exit Application', 'Are you sure you want to exit the application', icon='warning')
      if MsgBox == 'yes':
        self.destroy()
    def delete_student_data(self):
      MsgBox = mb.askquestion('Delete Record', 'Are you sure! you want to delete selected product record', icon='warning')
      if MsgBox == 'yes':
          if db_connection.is_connected() == False:
              db_connection.connect()
          db_cursor.execute("use prodotti")  # Interact with Student Database
          # deleteing selected student record
          Delete = "delete from prodotti where prodottoID='%s'" % (roll_no)
          db_cursor.execute(Delete)
          db_connection.commit()
          mb.showinfo("Information", "Student Record Deleted Succssfully")
          self.load_student_data()
          self.entFName.delete(0, tk.END)
          self.entLCode.delete(0, tk.END)
          self.entQuant.delete(0, tk.END)
          self.entPrice.delete(0, tk.END)
         




  

    def register_product(self):
        if db_connection.is_connected() == False:
          db_connection.connect()
        fname = self.entFName.get()  # Retrieving entered first name
        lname = self.entLName.get()  # Retrieving entered last name
        contact_no = self.entContact.get()  # Retrieving entered contact number
        city = self.entCity.get()  # Retrieving entered city name
        state = self.entState.get()  # Retrieving entered state name
        dob = self.calDOB.get()  # Retrieving choosen date
        # validating Entry Widgets
        if fname == "":
            mb.showinfo('Information', "Please Enter Nome")
            self.entFName.focus_set()
            return
        if lname == "":
            mb.showinfo('Information', "Please Enter Lastname")
            self.entLName.focus_set()
            return

        if contact_no == "":
            mb.showinfo('Information', "Please Enter Contact Number")
            self.entContact.focus_set()
            return
        if city == "":
            mb.showinfo('Information', "Please Enter City Name")
            self.entCity.focus_set()
            return
        if state == "":
            mb.showinfo('Information', "Please Enter State Name")
            self.entState.focus_set()
            return
        if dob == "":
            mb.showinfo('Information', "Please Choose Date of Birth")
            self.calDOB.focus_set()
            return


        # Inserting record into student_master table of student database
        try:
            rollno =int(self.fetch_max_roll_no())
            print("New Student Id: " + str(rollno))
            query2 = "INSERT INTO student_master (rollno, fname,lname,city,state,mobileno,dob) VALUES (%s, %s,%s, %s,%s, %s, %s)"
            # implement query Sentence
            db_cursor.execute(query2, (rollno, fname, lname, city, state, contact_no,dob))
            mb.showinfo('Information', "Student Registration Successfully")
            # Submit to database for execution
            db_connection.commit()
            self.load_student_data()
        except mysql.connector.Error as err:
            print(err)
            # Rollback in case there is any error
            db_connection.rollback()
            mb.showinfo('Information', "Data insertion failed!!!")
        finally:
           db_connection.close()

    def fetch_max_roll_no(self):
        if db_connection.is_connected() == False:
            db_connection.connect()
        db_cursor.execute("use prodotti")  # Interact with Student Database
        rollno  = 0
        query1 = "SELECT rollno FROM student_master order by  id DESC LIMIT 1"
        # implement query Sentence
        db_cursor.execute(query1)  # Retrieving maximum student id no
        print("No of Record Fetched:" + str(db_cursor.rowcount))
        if db_cursor.rowcount == 0:
            rollno = 1
        else:
            rows = db_cursor.fetchall()
            for row in rows:
                rollno = row[0]
            rollno = rollno + 1
        print("Max Student Id: " + str(rollno))
        return rollno

    def show_search_record(self):
        if db_connection.is_connected() == False:
            db_connection.connect()
        s_roll_no = self.entSearch.get()  # Retrieving entered first name
        print(s_roll_no)
        if  s_roll_no == "":
            mb.showinfo('Information', "Please Enter Student Roll")
            self.entSearch.focus_set()
            return
        self.tvProduct.delete(*self.tvProduct.get_children())  # clears the treeview tvProduct
        # Inserting record into student_master table of student database
        db_cursor.execute("use Student")  # Interact with Bank Database
        sql = "SELECT rollno,fname,lname,city,state,mobileno,date_format(dob,'%d-%m-%Y') FROM student_master where rollno='" + s_roll_no + "'"
        db_cursor.execute(sql)
        total = db_cursor.rowcount
        #if total ==0:
            #mb.showinfo("Info", "Nothing To Display,Please add data")
            #return
        print("Total Data Entries:" + str(total))
        rows = db_cursor.fetchall()

        RollNo = ""
        First_Name = ""
        Last_Name = ""
        City = ""
        State = ""
        Phone_Number = ""
        DOB =""
        for row in rows:
            RollNo = row[0]
            First_Name = row[1]
            Last_Name = row[2]
            City = row[3]
            State = row[4]
            Phone_Number = row[5]
            DOB = row[6]
            print( Phone_Number)
            self.tvProduct.insert("", 'end', text=RollNo, values=(RollNo, First_Name, Last_Name, City, State, Phone_Number,DOB))


    def show_selected_record(self, event):
        self.clear_form()
        for selection in self.tvProduct.selection():
            item = self.tvProduct.item(selection)
        global roll_no
        roll_no,first_name,last_name,city,state,contact_no,dob = item["values"][0:7]
        self.entFName.insert(0, first_name)
        self.entLName.insert(0, last_name)
        self.entCity.insert(0, city)
        self.entState .insert(0, state)
        self.entContact.insert(0, contact_no)
        self.calDOB.insert(0, dob)
        return roll_no

    def update_student_data(self):
        if db_connection.is_connected() == False:
            db_connection.connect()
        print("Updating")
        db_cursor.execute("use Student")  # Interact with Student Database
        First_Name = self.entFName.get()
        Last_Name = self.entLName.get()
        Phone_Number = self.entContact.get()
        City = self.entCity.get()
        State = self.entState.get()
        DOB = self.calDOB.get()
        print( roll_no)
        Update = "Update student_master set fname='%s', lname='%s', mobileno='%s', city='%s', state='%s', dob='%s' where rollno='%s'" % (
        First_Name, Last_Name, Phone_Number, City, State,DOB, roll_no)
        db_cursor.execute(Update)
        db_connection.commit()
        mb.showinfo("Info", "Selected Student Record Updated Successfully ")
        self.load_student_data()

    def load_student_data(self):
        if db_connection.is_connected() == False:
            db_connection.connect()
        self.calDOB.delete(0, tk.END)#clears the date entry widget
        self.tvProduct.delete(*self.tvProduct.get_children())  # clears the treeview tvProduct
        # Inserting record into student_master table of student database
        db_cursor.execute("use Student")  # Interact with Bank Database
        sql = "SELECT rollno,fname,lname,city,state,mobileno,date_format(dob,'%d-%m-%Y') FROM student_master"
        db_cursor.execute(sql)
        total = db_cursor.rowcount
        #if total ==0:
            #mb.showinfo("Info", "Nothing To Display,Please add data")
            #return
        print("Total Data Entries:" + str(total))
        rows = db_cursor.fetchall()

        RollNo = ""
        First_Name = ""
        Last_Name = ""
        City = ""
        State = ""
        Phone_Number = ""
        DOB =""
        for row in rows:
            RollNo = row[0]
            First_Name = row[1]
            Last_Name = row[2]
            City = row[3]
            State = row[4]
            Phone_Number = row[5]
            DOB = row[6]
            self.tvProduct.insert("", 'end', text=RollNo, values=(RollNo, First_Name, Last_Name, City, State, Phone_Number,DOB))



if __name__ == "__main__":
    app = StudentApp()
    app.mainloop()
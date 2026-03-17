import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *

def main_project():
    root = Tk()
    root.geometry("800x600")
    

    def GetValue(event):
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        row_name = listBox.selection()[0]
        select = listBox.set(row_name)
        e1.insert(0,select['name'])
        e2.insert(0,select['email'])
        e3.insert(0,select['phone'])
        e4.insert(0,select['address'])
     
     
    def Add():
        membername= e1.get()
        memberemail = e2.get()
        memberphone = e3.get()
        memberaddress = e4.get()
     
        mysqldb=mysql.connector.connect(host="localhost",user="root",password="Root@123",database="contact_management")
        mycursor=mysqldb.cursor()
     
        try:
           sql = "INSERT INTO  contacts (name,email,phone,address) VALUES (%s, %s, %s, %s)"
           val = (membername,memberemail,memberphone,memberaddress)
           mycursor.execute(sql, val)
           mysqldb.commit()
           lastid = mycursor.lastrowid
           messagebox.showinfo("information", "contacts inserted successfully...")
           e1.delete(0, END)
           e2.delete(0, END)
           e3.delete(0, END)
           e4.delete(0, END)
           e1.focus_set()
        except Exception as e:
           print(e)
           mysqldb.rollback()
           mysqldb.close()
     
     
    def update():
        membername= e1.get()
        memberemail = e2.get()
        memberphone = e3.get()
        memberaddress= e4.get()
        mysqldb=mysql.connector.connect(host="localhost",user="root",password="Root@123",database="contact_management")
        mycursor=mysqldb.cursor()
     
        try:
           sql = "Update  contacts set email= %s,phone= %s,address= %s where name= %s"
           val = (memberemail,memberphone,memberaddress,membername)
           mycursor.execute(sql, val)
           mysqldb.commit()
           lastid = mycursor.lastrowid
           messagebox.showinfo("information", "Record Updateddddd successfully...")
     
           e1.delete(0, END)
           e2.delete(0, END)
           e3.delete(0, END)
           e4.delete(0, END)
           e1.focus_set()
     
        except Exception as e:
     
           print(e)
           mysqldb.rollback()
           mysqldb.close()
     
    def delete():
        membername = e1.get()
     
        mysqldb=mysql.connector.connect(host="localhost",user="root",password="Root@123",database="contact_management")
        mycursor=mysqldb.cursor()
     
        try:
           sql = "delete from contacts where name = %s"
           val = (membername,)
           mycursor.execute(sql, val)
           mysqldb.commit()
           lastid = mycursor.lastrowid
           messagebox.showinfo("information", "Record Deleteeeee successfully...")
     
           e1.delete(0, END)
           e2.delete(0, END)
           e3.delete(0, END)
           e4.delete(0, END)
           e1.focus_set()
     
        except Exception as e:
     
           print(e)
           mysqldb.rollback()
           mysqldb.close()
     
    def show():
            mysqldb = mysql.connector.connect(host="localhost", user="root", password="Root@123", database="contact_management")
            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT name,email,phone,address FROM contacts")
            records = mycursor.fetchall()
            print(records)
     
            for i, (name,email, phone,address) in enumerate(records, start=1):
                listBox.insert("", "end", values=(name, email, phone, address))
                mysqldb.close()
     
    
    global e1
    global e2
    global e3
    global e4
     
    tk.Label(root, text="Contact Management", fg="red", font=(None, 30)).place(x=300, y=2)
     
    tk.Label(root, text="NAME").place(x=12, y=16)
    Label(root, text="EMAIL").place(x=14, y=44)
    Label(root, text="PHONE").place(x=16, y=76)
    Label(root, text="ADDRESS").place(x=18, y=112)
     
    e1 = Entry(root)
    e1.place(x=150, y=10)
     
    e2 = Entry(root)
    e2.place(x=150, y=40)
     
    e3 = Entry(root)
    e3.place(x=150, y=70)
     
    e4 = Entry(root)
    e4.place(x=150, y=100)
     
    Button(root, text="Add",command = Add,height=3, width= 13).place(x=30, y=130)
    Button(root, text="update",command = update,height=3, width= 13).place(x=140, y=130)
    Button(root, text="Delete",command = delete,height=3, width= 13).place(x=250, y=130)
     
    cols = ('name', 'email', 'phone','address')
    listBox = ttk.Treeview(root, columns=cols, show='headings' )
     
    for col in cols:
        listBox.heading(col, text=col)
        listBox.grid(row=1, column=0, columnspan=2)
        listBox.place(x=10, y=200)
     
    show()
    listBox.bind('<Double-Button-1>',GetValue)
     
    root.mainloop()
 


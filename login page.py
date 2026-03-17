from tkinter import*
import mysql.connector
import tkinter.messagebox as msg
from contactManagementSystem import main_project


class User:
    def __init__(self,root):
        self.root=root
        self.root.title("Home Page")
        self.root.geometry("400x400")
        
        
        title=Label(self.root,text="Welcome to Home page",font=('bold','15'))
        title.pack()
        
        register_button=Button(self.root,text="Register",command=self.register_page)
        register_button.place(x=150,y=100)

        login_button=Button(self.root,text="Login",command=self.login_page)
        login_button.place(x=150,y=200)

    def register_page(self):
        window=Tk()
        window.title("Registration page")
        window.geometry("400x400")
        
        
        username_label=Label(window,text="username:",font=('bold','20'))
        username_label.place(x=20,y=40)

        password_label=Label(window,text="password:",font=('bold','20'))
        password_label.place(x=20,y=80)

        email_label=Label(window,text="Email id:",font=('bold','20'))
        email_label.place(x=20,y=120)

        self.username_entry=Entry(window)
        self.username_entry.place(x=180,y=45)

        self.password_entry=Entry(window)
        self.password_entry.place(x=180,y=85)

        self.email_entry=Entry(window)
        self.email_entry.place(x=180,y=125)

        submit_register=Button(window,text="register",command=self.register_user)
        submit_register.place(x=150,y=250)

    def login_page(self):
        window1=Tk()
        window1.title("Login Page")
        window1.geometry("400x400")
        

        username_label=Label(window1,text="Username:",font=('bold','20'))
        username_label.place(x=20,y=70)

        password_label=Label(window1,text="Password:",font=('bold','20'))
        password_label.place(x=20,y=140)

        self.login_username=Entry(window1)
        self.login_username.place(x=180,y=70)

        self.login_password=Entry(window1)
        self.login_password.place(x=180,y=140)

        submit_login=Button(window1,text="Login",command=self.user_login)
        submit_login.place(x=150,y=200)

    def register_user(self):
        mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="Root@123",
        database="register_login"
    )
        mycursor=mydb.cursor()

        username=self.username_entry.get()
        password=self.password_entry.get()
        email=self.email_entry.get()

        mycursor.execute("insert into register values(%s,%s,%s)",(username,password,email))
        mydb.commit()

        msg.showinfo("Registration details","Registered successfully")

    def user_login(self):
        mydb=mysql.connector.connect(host='localhost',user='root',password='Root@123',database='register_login')
        mycursor=mydb.cursor()

        username1=self.login_username.get()
        password1=self.login_password.get()

        mycursor.execute("select * from register where username=%s and password=%s",(username1,password1))

        c=0
        for i in mycursor:
            c=c+1
        if c>=1:
            mycursor.execute(" insert into login values(%s,%s)",(username1,password1))
            mydb.commit()
            main_project()
        else:
            msg.showerror("login details","invalid user")



root=Tk()
obj=User(root)
root.mainloop()

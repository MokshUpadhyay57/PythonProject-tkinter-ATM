# ATM Project
# Author : Moksh Upadhyay
# Date : 1-6-2021

from tkinter import *
from tkinter import messagebox
from pymysql import *
import os


loginPage = Tk()
loginPage.title("Punjab National Bank")
loginPage.geometry("852x480")
loginPage.config(bg="Aqua") 

def login():
    user_name = log.get()
    password = pas.get()
    conn=connect(host='localhost',user='root',password='',db='atm')
    a=conn.cursor()
    a.execute("select * from login where username='"+user_name+"' and password='"+password+"'")
    conn.commit
    count=a.rowcount
    if(count>0):
        messagebox.showinfo("Log Message","Login Successful")
        os.system("E:\PROGRAMS\Python\PythonProject\maininterface.py")

    else:
        messagebox.showerror("Log Message","Invalid Username or Password")

# Heading 'Punjab National Bank'
header = Frame(loginPage,width=2000,height= 150,bg='yellow',bd=5,relief="raised")
header.pack(side="top",fill=BOTH)

# Label for Header
label_1 = Label(header,text="PUNJAB NATIONAL BANK",font=('arial',28,'bold'),height= 1,justify="center",fg="black",bg='yellow')
label_1.pack(side="top",ipadx=5,ipady=5)


# Body Frame
body = Frame(loginPage,width=350,height= 200,bg='yellow',bd=5,relief="raised")
body.pack(side="bottom",expand=True)


# Label for Username
label_1 = Label(body,text="Username",font=('arial',12,'bold'),height=1,bg='yellow')
label_1.place(x=35,y=35)
log = StringVar()

# Textbox for Login label
tb1=Entry(body,font=('arial',12,'bold'),textvariable=log)
tb1.place(x=130,y=35)


# Label for Password
label_2 = Label(body,text="Password",font=('arial',12,'bold'),bg='yellow',height= 1)
label_2.place(x=35,y=75)
pas = StringVar()

# Textbox for Password label
tb2=Entry(body,font=('arial',12,'bold'),show="*",textvariable=pas)
tb2.place(x=130,y=75)



button_submit = Button(body,text="Login",font=('arial',12,'bold'),bd=3,relief="raised",command=login)
button_submit.place(x=130,y=120)


loginPage.mainloop()
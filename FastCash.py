# ATM Project
# Author : Moksh Upadhyay
# Date : 4-6-2021

from tkinter import *
from tkinter import messagebox
import os
from datetime import datetime
import pymysql
fastcash = Tk()
fastcash.title("Punjab National Bank - Fast Cash Deposit")
fastcash.geometry("700x500")
fastcash.config(bg="lightblue")  

def FastCash200():
    acno=account.get()
    acpn=pin.get()
    amnt=200

    conn = pymysql.connect(host="localhost",user="root",password="",db='atm')
    var = conn.cursor()
    var.execute("select * from customer where Account='"+acno+"' and Pin='"+acpn+"' ")
    row=var.rowcount
    if(row>0):
        var.execute("update customer set amount=amount-'"+str(amnt)+"' where account='"+acno+"' and pin='"+acpn+"' ")
        
        var.execute("insert into mini (Account,Pin,Withdraw,Time) values('"+acno+"','"+acpn+"','"+str(amnt)+"','"+str(datetime.now())+"')")
        conn.commit()
        messagebox.showinfo("Log Info","Deposit successfull")
    else:
        messagebox.showinfo("Information","not valid")
        conn.rollback()
        messagebox.showinfo("Log Info","Deposit Unsuccessfull")

def FastCash500():
    acno=account.get()
    acpn=pin.get()
    amnt=500

    conn = pymysql.connect(host="localhost",user="root",password="",db='atm')
    var = conn.cursor()
    var.execute("select * from customer where Account='"+acno+"' and Pin='"+acpn+"' ")
    row=var.rowcount
    if(row>0):
        var.execute("update customer set amount=amount-'"+str(amnt)+"' where account='"+acno+"' and pin='"+acpn+"' ")
        
        var.execute("insert into mini (Account,Pin,Withdraw,Time) values('"+acno+"','"+acpn+"','"+str(amnt)+"','"+str(datetime.now())+"')")
        conn.commit()
        messagebox.showinfo("Log Info","Deposit successfull")
    else:
        messagebox.showinfo("Information","not valid")
        conn.rollback()
        messagebox.showinfo("Log Info","Deposit Unsuccessfull")

def FastCash1000():
    acno=account.get()
    acpn=pin.get()
    amnt=1000

    conn = pymysql.connect(host="localhost",user="root",password="",db='atm')
    var = conn.cursor()
    var.execute("select * from customer where Account='"+acno+"' and Pin='"+acpn+"' ")
    row=var.rowcount
    if(row>0):
        var.execute("update customer set amount=amount-'"+str(amnt)+"' where account='"+acno+"' and pin='"+acpn+"' ")
        
        var.execute("insert into mini (Account,Pin,Withdraw,Time) values('"+acno+"','"+acpn+"','"+str(amnt)+"','"+str(datetime.now())+"')")
        conn.commit()
        messagebox.showinfo("Log Info","Deposit successfull")
    else:
        messagebox.showinfo("Information","not valid")
        conn.rollback()
        messagebox.showinfo("Log Info","Deposit Unsuccessfull")


def FastCash2000():
    acno=account.get()
    acpn=pin.get()
    amnt=2000

    conn = pymysql.connect(host="localhost",user="root",password="",db='atm')
    var = conn.cursor()
    var.execute("select * from customer where Account='"+acno+"' and Pin='"+acpn+"' ")
    row=var.rowcount
    if(row>0):
        var.execute("update customer set amount=amount-'"+str(amnt)+"' where account='"+acno+"' and pin='"+acpn+"' ")
        
        var.execute("insert into mini (Account,Pin,Withdraw,Time) values('"+acno+"','"+acpn+"','"+str(amnt)+"','"+str(datetime.now())+"')")
        conn.commit()
        messagebox.showinfo("Log Info","Deposit successfull")
    else:
        messagebox.showinfo("Information","not valid")
        conn.rollback()
        messagebox.showinfo("Log Info","Deposit Unsuccessfull")

# Heading
header = Frame(fastcash,width=2000,height= 150,bg='yellow',bd=5,relief="raised")
header.pack(side="top",fill=BOTH)

# Label for Header
label_1 = Label(header,text="PUNJAB NATIONAL BANK",font=('arial',28,'bold'),height= 1,justify="center",fg="black",bg="yellow")
label_1.pack(side="top",ipadx=5,ipady=5)



# Body Frame
body = Frame(fastcash,width=440,height= 250,bg='yellow',bd=5,relief="raised")
body.pack(side="bottom",expand=True)

# Customer Account Number
Account = Label(body, text="Enter Account No",font=('arial',12,'bold'),bg='yellow')
Account.place(x=50,y=30)
account = StringVar()

# Textbox for Account Number
tb1=Entry(body,font=('arial',12,'bold'),textvariable=account)
tb1.place(x=200,y=30)

# Account Pin
Pin = Label(body, text="Enter Pin",font=('arial',12,'bold'),bg='yellow')
Pin.place(x=50,y=70)
pin = StringVar()

# Texbox for Account Pin
tb1=Entry(body,font=('arial',12),textvariable=pin)
tb1.place(x=200,y=70)

# Fast Cash Buttons
# 200 Rs Button
Button_1 = Button(body, text="200",font=('arial',12,'bold'), width=8,bd=5,height=1,relief="raised",command=FastCash200)
Button_1.place(x=65,y=120)

# 500 Rs Button
Button_1 = Button(body, text="500",font=('arial',12,'bold'), width=8,bd=5,height=1,relief="raised",command=FastCash500)
Button_1.place(x=250,y=120)

# 1000 Rs Button
Button_1 = Button(body, text="1000",font=('arial',12,'bold'), width=8,bd=5,height=1,relief="raised",command=FastCash1000)
Button_1.place(x=65,y=170)

# 2000 Rs Button
Button_1 = Button(body, text="2000",font=('arial',12,'bold'), width=8,bd=5,height=1,relief="raised",command=FastCash2000)
Button_1.place(x=250,y=170)

fastcash.mainloop()
# ATM Project
# Author : Moksh Upadhyay
# Date : 3-6-2021

from tkinter import *
from tkinter import messagebox
import os
from pymysql import *

balance = Tk()
balance.title("Punjab National Bank - Check Balance")
balance.geometry("750x500")
balance.config(bg="lightblue") 

def Balance():
    acno=account.get()
    acpn=int(pin.get())
    try:
        conn=connect(host='localhost',user='root',password='',db='atm')
        a=conn.cursor()
        query = "select * from customer where Account = %s and Pin = %s"
        values = (acno,acpn)
        a.execute(query,values)
        conn.commit
        results=a.fetchall()
        count=a.rowcount
        if(count>0):
            for row in results:
                for i in range(0,count):
                    messagebox.showinfo("Log Message", row[5])
        else:
            messagebox.showerror("Log Message","account not found")
    except:
        conn.rollback()
        print('Log Message','Error in searching')
    conn.close()

# Heading
header = Frame(balance,width=2000,height= 150,bg='yellow',bd=5,relief="raised")
header.pack(side="top",fill=BOTH)

# Label for Header
label_1 = Label(header,text="PUNJAB NATIONAL BANK",font=('arial',28,'bold'),height= 1,justify="center",fg="black",bg="yellow")
label_1.pack(side="top",ipadx=5,ipady=5)


# Body Frame
body = Frame(balance,width=450,height= 200,bg='yellow',bd=5,relief="raised")
body.pack(side="bottom",expand=True)

# Customer Account Number
Account = Label(body, text="Enter Account no",font=('arial',12,'bold'),bg='yellow')
Account.place(x=40,y=30)
account = StringVar()

# Textbox for Account Number
tb1=Entry(body,font=('arial',12,'bold'),textvariable=account)
tb1.place(x=220,y=30)


# Account Pin
Pin = Label(body, text="Enter Pin",font=('arial',12,'bold'),bg='yellow')
Pin.place(x=100,y=70)
pin = StringVar()

# Texbox for Account Pin
tb1=Entry(body,font=('arial',12,'bold'),show="*",textvariable=pin)
tb1.place(x=220,y=70)

# Balance Button
Button_1 = Button(body, text="Check Balance",font=('arial',12,'bold'), width=12,bd=5,height=1,padx=2,pady=2,relief="raised",command=Balance)
Button_1.place(x=150,y=120)

balance.mainloop()

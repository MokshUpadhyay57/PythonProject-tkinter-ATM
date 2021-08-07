# ATM Project
# Author : Moksh Upadhyay
# Date : 3-6-2021

from tkinter import *
from tkinter import messagebox
import os
from pymysql import *
from datetime import datetime

withdraw = Tk()
withdraw.title("Punjab National Bank")
withdraw.geometry("700x500")
now = datetime.now()
withdraw.config(bg="lightblue")  

def Withdraw():
    acno=account.get()
    acpn=pin.get()
    amnt=int(amount.get())
    conn=connect(host='localhost',user='root',password='',database='atm')
    a=conn.cursor()
    a.execute("select * from customer where Account='"+acno+"' and Pin='"+acpn+"' ")
    row = a.rowcount
    if(row>0):
        values1=(amnt,acno,acpn)
        query="update customer set Amount = Amount - %s where Account=%s and Pin=%s"
        a.execute(query,values1)
        query="insert into mini (Account,Pin,Withdraw,Time) values (%s,%s,%s,%s)"
        values2=(acno,acpn,amnt,datetime.now())
        a.execute(query,values2)
        conn.commit()
        messagebox.showinfo("Log Message","Amount withdrawl Successful")
    else:
        conn.rollback()
        messagebox.showerror("Log Message",'Amount withdrawl is not successful!!!')
    conn.close()

# Heading
header = Frame(withdraw,width=2000,height= 150,bg='yellow',bd=5,relief="raised")
header.pack(side="top",fill=BOTH)

# Label for Header
label_1 = Label(header,text="PUNJAB NATIONAL BANK",font=('arial',28,'bold'),height= 1,justify="center",fg="black",bg="yellow")
label_1.pack(side="top",ipadx=5,ipady=5)


# Body Frame
body = Frame(withdraw,width=450,height= 250,bg='yellow',bd=5,relief="raised")
body.pack(side="bottom",expand=True)

# Customer Account Number
label_1 = Label(body, text="Enter Account No",font=('arial',12,'bold'),bg="yellow")
label_1.place(x=50,y=30)
account = StringVar()

# Textbox for Account Number
tb1=Entry(body,font=('arial',12,'bold'),textvariable=account)
tb1.place(x=220,y=30)

# Account Pin
label_2 = Label(body, text="Enter Pin",font=('arial',12,'bold'),bg="yellow")
label_2.place(x=50,y=70)
pin = StringVar()

# Texbox for Account Pin
tb2=Entry(body,font=('arial',12,'bold'),show="*",textvariable=pin)
tb2.place(x=220,y=70)

# Amount to be deducted(withdraw)
label_3 = Label(body, text="Enter Amount",font=('arial',12,'bold'),bg="yellow")
label_3.place(x=50,y=110)
amount = StringVar()

# TextBox for Amount
tb3=Entry(body,font=('arial',12,'bold'),textvariable=amount)
tb3.place(x=220,y=110)

# Withdraw Button
Button_1 = Button(body, text="Withdraw Cash",font=('arial',12,'bold'), width=12,bd=5,height=1,padx=4,pady=5,relief="raised",command=Withdraw)
Button_1.place(x=140,y=170)

withdraw.mainloop()
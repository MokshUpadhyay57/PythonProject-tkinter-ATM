# ATM Project
# Author : Moksh Upadhyay
# Date : 3-6-2021

from tkinter import *
from tkinter import messagebox
import os,pymysql
from datetime import datetime
transfer = Tk()
transfer.title("Punjab National Bank")
transfer.geometry("800x600")
transfer.config(bg="skyblue") 

def Transfer():
    acno=acc.get()
    ac = account1.get()
    acpn=pin.get()
    amnt=int(amount.get())
    code = ifsc.get()

    conn=pymysql.connect(host='localhost',user='root',password='',database='atm')
    
    a=conn.cursor()
    a.execute("select * from customer where account='"+acno+"' and pin='"+acpn+"' ")
    row = a.rowcount
    if(row>0):
        a.execute("update customer set Amount=Amount-'"+str(amnt)+"' where Account='"+acno+"' and Pin='"+acpn+"' ")
        a.execute("insert into mini (Account,Pin,Withdraw,Time) values('"+acno+"','"+acpn+"','"+str(amnt)+"','"+str(datetime.now())+"')")
        
        a.execute("update unionbank set amount=amount+'"+str(amnt)+"' where account='"+ac+"' and ifsc='"+code+"' ")
        conn.commit()
        messagebox.showinfo("Log Message","Fund Transfer Successful")
    else:
        conn.rollback()
        messagebox.showerror("Log Message",'Fund Transfer Failed')
    conn.close() 
         

# Heading
header = Frame(transfer,width=2000,height= 150,bg='yellow',bd=5,relief="raised")
header.pack(side="top",fill=BOTH)

# Label for Header
label_1 = Label(header,text="PUNJAB NATIONAL BANK",font=('arial',28,'bold'),height= 1,justify="center",fg="black",bg="yellow")
label_1.pack(side="top",ipadx=5,ipady=5)




# Body Frame
body = Frame(transfer,width=480,height= 330,bg='yellow',bd=5,relief="raised")
body.pack(side="bottom",expand=True)

# Customer Account Number
label_1 = Label(body, text="Enter Account no from ",font=('arial',12,'bold'),bg='yellow')
label_1.place(x=50,y=40)
acc = StringVar()

# Textbox for Account Number
tb1=Entry(body,font=('arial',12,'bold'),textvariable=acc)
tb1.place(x=240,y=40)

# Account Pin
label_2 = Label(body, text="Enter Pin",font=('arial',12,'bold'),bg='yellow')
label_2.place(x=50,y=80)
pin = StringVar()

# Textbox for Account Pin
tb2=Entry(body,font=('arial',12,'bold'),show="*",textvariable=pin)
tb2.place(x=240,y=80)

# Amount to be Added
label_3 = Label(body, text="Enter Amount",font=('arial',12,'bold'),bg='yellow')
label_3.place(x=50,y=120)
amount = StringVar()

# TextBox for Amount
tb3=Entry(body,font=('arial',12,'bold'),textvariable=amount)
tb3.place(x=240,y=120)


# Receiver Account Number
label_4 = Label(body, text="Enter Account no to ",font=('arial',12,'bold'),bg='yellow')
label_4.place(x=50,y=160)
account1 = StringVar()

# Textbox for Account Number
tb4=Entry(body,font=('arial',12,'bold'),textvariable=account1)
tb4.place(x=240,y=160)

# IFSC Number
label_5 = Label(body, text="Enter IFSC Number ",font=('arial',12,'bold'),bg='yellow')
label_5.place(x=50,y=200)
ifsc = StringVar()

# Textbox for IFSC Number
tb5=Entry(body,font=('arial',12,'bold'),textvariable=ifsc)
tb5.place(x=240,y=200)

# Transfer Button
Button_1 = Button(body, text="Transfer Fund",font=('arial',12,'bold'), width=11,bd=5,height=1,padx=4,pady=5,relief="raised",command=Transfer)
Button_1.place(x=160,y=250)

transfer.mainloop()
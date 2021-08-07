# ATM Project
# Author : Moksh Upadhyay
# Date : 4-6-2021

from tkinter import *
from tkinter import messagebox
import os
import pymysql

changePin = Tk()
changePin.title("Punjab National Bank - Change Pin")
changePin.geometry("800x600")
changePin.config(bg="skyblue") 

def Change():
    acno=account.get()
    opa=int(op.get())
    npa=int(np.get())
    cpa = int(cp.get())
    try:
        if(npa==cpa):
            conn=pymysql.connect(host='localhost',user='root',password='',db='atm')
            a=conn.cursor()
            a.execute("update customer set Pin='"+str(npa)+"' where Account='"+str(acno)+"' and Pin='"+str(opa)+"'")

            conn.commit()
            messagebox.showinfo("message"," Password change Successful")
        else:
            messagebox.showerror("message","Password Change Failed")
    except:
            conn.rollback()
            messagebox.showerror("message","Database Error")
            conn.close()


# Heading
header = Frame(changePin,width=2000,height= 150,bg='yellow',bd=5,relief="raised")
header.pack(side="top",fill=BOTH)

# Label for Header
label_1 = Label(header,text="PUNJAB NATIONAL BANK",font=('arial',28,'bold'),height= 1,justify="center",fg="black",bg="yellow")
label_1.pack(side="top",ipadx=5,ipady=5)


# Body Frame
body = Frame(changePin,width=460,height= 280,bg='yellow',bd=5,relief="raised")
body.pack(side="bottom",expand=True)

# Customer Account Number
Account = Label(body, text="Enter Account No",font=('arial',12,'bold'))
Account.place(x=40,y=30)
account = StringVar()

# Textbox for Account Number
tb1=Entry(body,font=('arial',12,'bold'),textvariable=account)
tb1.place(x=230,y=30)

# Old Account Pin
Pin = Label(body, text="Enter Old Pin",font=('arial',12,'bold'))
Pin.place(x=40,y=70)
op = StringVar()

# Texbox for  Old Account Pin
tb1=Entry(body,font=('arial',12,'bold'),textvariable=op)
tb1.place(x=230,y=70)

# New Account Pin
Pin = Label(body, text="Enter New Pin",font=('arial',12,'bold'))
Pin.place(x=40,y=110)
np = StringVar()

# Texbox for New Account Pin
tb1=Entry(body,font=('arial',12,'bold'),textvariable=np)
tb1.place(x=230,y=110)

# Confirm New Account Pin
Pin = Label(body, text="Confirm New Pin",font=('arial',12,'bold'))
Pin.place(x=40,y=150)
cp = StringVar()

# Textbox for New Account Pin
tb1=Entry(body,font=('arial',12,'bold'),textvariable=cp)
tb1.place(x=230,y=150)

# Change Pin Button
Button_1 = Button(body, text="Change Pin",font=('arial',12,'bold'), width=10,bd=5,height=1,relief="raised",command=Change)
Button_1.place(x=155,y=200)

changePin.mainloop()
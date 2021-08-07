# ATM Project
# Author : Moksh Upadhyay
# Date : 4-6-2021

from tkinter import *
from tkinter import messagebox
import os
import pymysql

updateContact = Tk()
updateContact.title("Punjab National Bank")
updateContact.geometry("800x600")
updateContact.config(bg="skyblue") 

def Update():
    acno=account.get()
    acpn=int(pin.get())
    cn=int(contact.get())
    ncn = int(contactnew.get())
    ccn = int(confirmcontact.get())
    try:
        if(ncn==ccn):
            conn=pymysql.connect(host='localhost',user='root',password='',db='atm')
            a=conn.cursor()
            a.execute("update customer set Contact='"+str(ncn)+"' where Account='"+acno+"' and Pin='"+str(acpn)+"' and Contact = '"+str(cn)+"'")

            conn.commit()
            messagebox.showinfo("Log Info"," Contact Update Success")
        else:
            messagebox.showerror("Log Info","Contact Update Failed")
    except:
            conn.rollback()
            messagebox.showerror("Log Info","Database Error")
            conn.close()

# Heading
header = Frame(updateContact,width=2000,height= 150,bg='yellow',bd=5,relief="raised")
header.pack(side="top",fill=BOTH)

# Label for Header
label_1 = Label(header,text="PUNJAB NATIONAL BANK",font=('arial',28,'bold'),height= 1,justify="center",fg="black",bg="yellow")
label_1.pack(side="top",ipadx=5,ipady=5)


# Body Frame
body = Frame(updateContact,width=520,height= 330,bg='yellow',bd=5,relief="raised")
body.pack(side="bottom",expand=True)

# Customer Account Number
Account = Label(body, text="Enter Account No",font=('arial',12,'bold'),bg='yellow')
Account.place(x=40,y=30)
account = StringVar()

# Textbox for Account Number
tb1=Entry(body,font=('arial',12,'bold'),textvariable=account)
tb1.place(x=280,y=30)

# Account Pin
label_2 = Label(body, text="Enter Pin",font=('arial',12,'bold'),bg='yellow')
label_2.place(x=40,y=70)
pin = StringVar()

# Texbox for Account Pin
tb2=Entry(body,font=('arial',12,'bold'),show="*",textvariable=pin)
tb2.place(x=280,y=70)


# Old Contact Number
oldcontactnumber = Label(body, text="Enter Old Contact Number",font=('arial',12,'bold'),bg='yellow')
oldcontactnumber.place(x=40,y=110)
contact = StringVar()

# Texbox for  Old Contact Number
tb1=Entry(body,font=('arial',12,'bold'),textvariable=contact)
tb1.place(x=280,y=110)

# New Contact Number
newcontactnumber = Label(body, text="Enter New Contact Number",font=('arial',12,'bold'),bg='yellow')
newcontactnumber.place(x=40,y=150)
contactnew = StringVar()

# Texbox for New Contact Number
tb1=Entry(body,font=('arial',12,'bold'),textvariable=contactnew)
tb1.place(x=280,y=150)

# Confirm New Contact Number
confirmContactNumber = Label(body, text="Confirm New Contact Number",font=('arial',12,'bold'),bg='yellow')
confirmContactNumber.place(x=40,y=190)
confirmcontact = StringVar()
 
# Textbox for New Contact Number
tb1=Entry(body,font=('arial',12,'bold'),textvariable=confirmcontact)
tb1.place(x=280,y=190)

# Change Pin Button
Button_1 = Button(body, text="Update",font=('arial',12,'bold'), width=10,bd=5,height=1,relief="raised",command=Update)
Button_1.place(x=190,y=250)

updateContact.mainloop()
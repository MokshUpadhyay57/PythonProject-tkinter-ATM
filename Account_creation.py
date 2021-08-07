# ATM Project
# Author : Moksh Upadhyay
# Date : 4-6-2021

from tkinter import *
from tkinter import messagebox
from pymysql import *
CreateUser = Tk()
CreateUser.title("Punjab National Bank - Account Creation")
CreateUser.geometry("900x700")
CreateUser.config(bg="Aqua") 


def Add(): 
    acno=ac.get()
    acnm = name.get()
    amnt = amount.get()
    add = address.get()
    cn = int(contact.get())
    acpn = pin.get()
    try:
        conn=connect(host='localhost',user='root',password='',db='atm')
        a=conn.cursor()
        a.execute("insert into customer(Account,Name,Address,Contact,Pin,Amount) values ('"+acno+"','"+acnm+"','"+add+"','"+str(cn)+"','"+acpn+"','"+amnt+"')")
        conn.commit()
        messagebox.showinfo("message","Account Created Succesfully")
    except:
            conn.rollback()
            messagebox.showerror("message","Error!!! Account Creation Failed")
            conn.close()

def Delete():
    acno=ac.get()
    try:
        conn=connect(host='localhost',user='root',password='',db='atm')
        a=conn.cursor()
        a.execute("DELETE FROM customer WHERE Account = '"+acno+"'")
        conn.commit()
        messagebox.showinfo("message","Customer Added Succesfully")
    except:
        conn.rollback()
        messagebox.showerror("message","Error!!! Customer not added")
        conn.close()

def Update():
    acno=ac.get()
    acnm = name.get()
    amnt = amount.get()
    add = address.get()
    cn = int(contact.get())
    acpn = pin.get()
    try:
        conn=connect(host='localhost',user='root',password='',db='atm')
        a=conn.cursor()
        a.execute("UPDATE customer set Name = '"+acnm+"' and Address = '"+add+"' and Amount = '"+amnt+"' and Contact = '"+str(cn)+"' Pin = '"+str(acpn)+"'WHERE Account = '"+acno+"'")
        a.execute()
        conn.commit()
        messagebox.showinfo("message","Details Updated Succesfully")
    except:
            conn.rollback()
            messagebox.showerror("message","Error!!! Details Not Updated")
            conn.close()


def ShowAllData():
    acno=ac.get()
    conn = connect(host="localhost",user="root",password="",db='atm')
    var = conn.cursor()
    var.execute("select * from customer")
    v = var.fetchall()
    show = Tk()
    show.geometry("1200x900")
    show.resizable(False,True)
    show.title("Punjab National Bank - Customers List")
    vary=80
    #-------------------------------Label of the Table---------------------------------#
    lb1 = Label(show,text="Account ",width=16,font=("Tines New Roman",12,"bold"),bg="white",bd=5).place(x=40,y=50)
    lb2 = Label(show,text="Name",width=16,font=("Tines New Roman",12,"bold"),bg="white",bd=5).place(x=230,y=50)
    lb3 = Label(show,text="Address",width=16,font=("Tines New Roman",12,"bold"),bg="white",bd=5).place(x=420,y=50)
    lb4 = Label(show,text="Contact",width=16,font=("Tines New Roman",12,"bold"),bg="white",bd=5).place(x=610,y=50)
    lb5 = Label(show,text="Pin ",width=16,font=("Tines New Roman",12,"bold"),bg="white",bd=5).place(x=800,y=50) 
    lb6 = Label(show,text="Amount ",width=16,font=("Tines New Roman",12,"bold"),bg="white",bd=5).place(x=990,y=50)

    for i in range(0,var.rowcount):
        lb1 = Label(show,text=v[i][0],width=16,font=("Tines New Roman",12,"bold"),bg="white",bd=5).place(x=40,y=vary)
        lb2 = Label(show,text=v[i][1],width=16,font=("Tines New Roman",12,"bold"),bg="white",bd=5).place(x=230,y=vary)
        lb3 = Label(show,text=v[i][2],width=16 ,font=("Tines New Roman",12,"bold"),bg="white",bd=5).place(x=420,y=vary)
        lb4 = Label(show,text=v[i][3],width=16,font=("Tines New Roman",12,"bold"),bg="white",bd=5).place(x=610,y=vary)
        lb5 = Label(show,text=v[i][4],width=16,font=("Tines New Roman",12,"bold"),bg="white",bd=5).place(x=800,y=vary)
        lb6 = Label(show,text=v[i][5],width=16,font=("Tines New Roman",12,"bold"),bg="white",bd=5).place(x=990,y=vary)
        vary+=30
        conn.commit()



# Heading 'Punjab National Bank'
header = Frame(CreateUser,width=2000,height= 150,bg='yellow',bd=5,relief="raised")
header.pack(side="top",fill=BOTH)

# Label for Header
label_1 = Label(header,text="PUNJAB NATIONAL BANK",font=('arial',28,'bold'),height= 1, bg="yellow",fg="black")
label_1.pack(side="top",ipadx=5,ipady=5)

# Main Body
body = Frame(CreateUser,width=520,height= 530,bg='yellow',bd=5,relief="raised")
body.pack(side="bottom",expand=True)

# Heading of Body Frame
Heading = Label(body,text="Enter the following Customer Details",bg='yellow',font=('arial',14,'bold'),height= 1,justify="center")
Heading.place(x=100,y=30)


# Customer Account Number
acc = Label(body, text="Enter Account No",font=('arial',12,'bold'),bg='yellow')
acc.place(x=75,y=90)
ac = StringVar()

tb1=Entry(body,font=('arial',12,'bold'),textvariable=ac)
tb1.place(x=250,y=90)

# Customer Name
Name = Label(body, text="Enter Name",font=('arial',12,'bold'),bg='yellow')
Name.place(x=75,y=140)
name = StringVar()

tb2=Entry(body,font=('arial',12,'bold'),textvariable=name)
tb2.place(x=250,y=140)


# Customer Amount to deposit
Amount = Label(body, text="Enter Amount",font=('arial',12,'bold'),bg='yellow')
Amount.place(x=75,y=190)
amount = StringVar()

tb3=Entry(body,font=('arial',12,'bold'),textvariable=amount)
tb3.place(x=250,y=190)


# Address of Customer
Address = Label(body, text="Enter Address",font=('arial',12,'bold'),bg='yellow')
Address.place(x=75,y=240)
address = StringVar()

tb4=Entry(body,font=('arial',12,'bold'),textvariable=address)
tb4.place(x=250,y=240)

# Contact of Customer
Contact = Label(body, text="Enter Contact",font=('arial',12,'bold'),bg='yellow')
Contact.place(x=75,y=290)
contact = StringVar()

tb4=Entry(body,font=('arial',12,'bold'),textvariable=contact)
tb4.place(x=250,y=290)


# # Pin for Customer Account 
Pin = Label(body, text="Enter Pin",font=('arial',12,'bold'),bg='yellow')
Pin.place(x=75,y=340)
pin = StringVar()

tb4=Entry(body,font=('arial',12,'bold'),show='*',textvariable=pin)
tb4.place(x=250,y=340)

# Account Creation Buttons
# Add Button
Button_1 = Button(body, text="Add",font=('arial',12,'bold'), width=8,bd=4,height=1,relief="raised",command=Add)
Button_1.place(x=90,y=385)

# Delete Button
Button_1 = Button(body, text="Delete",font=('arial',12,'bold'), width=8,bd=4,height=1,relief="raised",command=Delete)
Button_1.place(x=200,y=385)

# Update Button
Button_1 = Button(body, text="Update",font=('arial',12,'bold'), width=8,bd=4,height=1,relief="raised",command=Update)
Button_1.place(x=310,y=385)

# Show all Data Button
Button_1 = Button(body, text="Show All Customers",font=('arial',12,'bold'), width=17,bd=5,height=1,relief="raised",command=ShowAllData)
Button_1.place(x=150,y=440)

CreateUser.mainloop()
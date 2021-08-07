# ATM Project
# Author : Moksh Upadhyay
# Date : 30-05-2021

from tkinter import *
from tkinter import messagebox
import os

main = Tk()
main.title("Punjab National Bank")
main.geometry("900x600")
main.config(bg="lightblue")  

def deposit():
    os.system("E:\PROGRAMS\Python\PythonProject\Deposit.py")

def withdraw():
    os.system("E:\PROGRAMS\Python\PythonProject\Withdraw.py")

def balance():
    os.system("E:\PROGRAMS\Python\PythonProject\Balance.py")

def transfer():
    os.system("E:\PROGRAMS\Python\PythonProject\TransferInterface.py")

def ministatement():
    os.system("MiniStatement.py")

def fastcash():
    os.system("E:\PROGRAMS\Python\PythonProject\FastCash.py")

def changePin():
    os.system("E:\PROGRAMS\Python\PythonProject\ChangePin.py")

def updateContact():
    os.system("E:\\PROGRAMS\\Python\\PythonProject\\UpdateContact.py")

# Heading 
header = Frame(main,width=2000,height= 150,bg='yellow',bd=5,relief="raised")
header.pack(side="top",fill=BOTH)
label_1 = Label(header,text="PUNJAB NATIONAL BANK",font=('arial',28,'bold'),height= 1,justify="center",fg="black",bg='yellow')
label_1.pack(side="top",ipadx=5,ipady=5)

# Body Frame
body = Frame(main,width=410,height= 310,bg='yellow',bd=5,relief="raised")
body.pack(side="bottom",expand=True)

# Deposit Button
Button_1 = Button(body, text="Deposit Cash",font=('Arial',12,'bold'), bd=5, width=12,height=1,padx=4,pady=5,command=deposit)
Button_1.place(x=30,y=30)

# Withdraw Button
Button_2 = Button(body, text="Withdraw Cash",font=('Arial',12,'bold'), bd=5,width=12,height=1,padx=4,pady=5,command=withdraw)
Button_2.place(x=30,y=95)

# Balance Enquiry Button
Button_3 = Button(body, text="Balance Enquiry",font=('Arial',12,'bold'), bd=5, width=12,height=1,padx=4,pady=5,command=balance)
Button_3.place(x=30,y=160)

# Transfer Fund Button
Button_4 = Button(body, text="Fund Transfer",font=('Arial',12,'bold'), bd=5,width=12,height=1,padx=4,pady=5,command=transfer)
Button_4.place(x=30,y=225)



# Mini Statement Button
Button_5 = Button(body, text="Mini Statement",font=('Arial',12,'bold'), bd=5, width=12,height=1,padx=4,pady=5,command=ministatement)
Button_5.place(x=220,y=30)

# Fast Cash Button
Button_6 = Button(body, text="Fast Cash",font=('Arial',12,'bold'), bd=5,width=12,height=1,padx=4,pady=5,command=fastcash)
Button_6.place(x=220,y=95)

# Chane Pin Button
Button_7 = Button(body, text="Change Pin",font=('Arial',12,'bold'), bd=5, width=12,height=1,padx=4,pady=5,command=changePin)
Button_7.place(x=220,y=160)

# Update Contact Button
Button_8 = Button(body, text="Update Contact",font=('Arial',12,'bold'), bd=5,width=12,height=1,padx=4,pady=5,command=updateContact)
Button_8.place(x=220,y=225)

main.mainloop()
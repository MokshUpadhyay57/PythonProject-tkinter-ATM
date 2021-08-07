# ATM Project
# Author : Moksh Upadhyay
# Date : 07-07-2021

from tkinter import *
from tkinter import messagebox
import os
tfInterface = Tk()
tfInterface.title("Punjab National Bank - Fund Transfer")
tfInterface.geometry("500x400")
tfInterface.config(bg="skyblue") 

def hdfc():
    os.system("E:\PROGRAMS\Python\PythonProject\Transferhdfc.py")

def state():
    os.system("E:\PROGRAMS\Python\PythonProject\Transferstate.py")


def union():
    os.system("E:\PROGRAMS\Python\PythonProject\Transferunion.py")


def icici():    
    os.system("E:\PROGRAMS\Python\PythonProject\Transfericici.py")


# Label for Header
label_1 = Label(tfInterface,text="Select Bank",font=('Times New Roman',20,'bold'),height= 1,justify="center",fg="black",bg="skyblue")
label_1.place(x=185,y = 25)

# Body Frame
body = Frame(tfInterface,width=360,height= 210,bg='yellow',bd=5,relief="raised")
body.pack(side="bottom",expand=True)

Button_1 = Button(body, text="HDFC Bank",font=('arial',12,'bold'), width=12,bd=4,height=1,padx=2,pady=2,relief="raised",command=hdfc)
Button_1.place(x=25,y=40)

Button_2 = Button(body, text="State Bank",font=('arial',12,'bold'), width=12,bd=4,height=1,padx=2,pady=2,relief="raised",command=state)
Button_2.place(x=25,y=120)

Button_3 = Button(body, text="Union Bank",font=('arial',12,'bold'), width=12,bd=4,height=1,padx=2,pady=2,relief="raised",command=union)
Button_3.place(x=190,y=40)

Button_4 = Button(body, text="ICICI Bank",font=('arial',12,'bold'), width=12,bd=4,height=1,padx=2,pady=2,relief="raised",command=icici)
Button_4.place(x=190,y=120)
tfInterface.mainloop()
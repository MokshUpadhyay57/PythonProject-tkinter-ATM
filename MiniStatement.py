# ATM Project
# Author : Moksh Upadhyay
# Date : 3-6-2021

from tkinter import *
from pymysql import *

statement = Tk()
statement.title("Punjab National Bank")
statement.geometry("700x400")
statement.config(bg="lightblue") 

def Statement():
        if True:
            acno=account.get()
            conn = connect(host="localhost",user="root",password="",db='atm')
            var = conn.cursor()
            var.execute("select * from mini where account='"+acno+"'")
            v = var.fetchall()
            show = Tk()
            show.geometry("1000x900")
            show.resizable(False,True)
            show.title("Punjab National Bank - E-Statement")
            vary=80
            #-------------------------------Label of the Table---------------------------------#
            lb1 = Label(show,text="Account ",width=16,font=("Tines New Roman",12,"bold"),bg="white",bd=5).place(x=40,y=50)
            lb2 = Label(show,text="Pin",width=16,font=("Tines New Roman",12,"bold"),bg="white",bd=5).place(x=230,y=50)
            lb3 = Label(show,text="Withdrawl",width=16,font=("Tines New Roman",12,"bold"),bg="white",bd=5).place(x=420,y=50)
            lb4 = Label(show,text="Deposit",width=16,font=("Tines New Roman",12,"bold"),bg="white",bd=5).place(x=610,y=50)
            lb5 = Label(show,text="Time ",width=16,font=("Tines New Roman",12,"bold"),bg="white",bd=5).place(x=800,y=50)

            for i in range(0,var.rowcount):
                lb1 = Label(show,text=v[i][0],width=16,font=("Tines New Roman",12,"bold"),bg="white",bd=5).place(x=40,y=vary)
                lb2 = Label(show,text=v[i][1],width=16,font=("Tines New Roman",12,"bold"),bg="white",bd=5).place(x=230,y=vary)
                lb3 = Label(show,text=v[i][2],width=16,font=("Tines New Roman",12,"bold"),bg="white",bd=5).place(x=420,y=vary)
                lb4 = Label(show,text=v[i][3],width=16,font=("Tines New Roman",12,"bold"),bg="white",bd=5).place(x=610,y=vary)
                lb5 = Label(show,text=v[i][4],width=16,font=("Tines New Roman",12,"bold"),bg="white",bd=5).place(x=800,y=vary)
                vary+=30
            conn.commit()
        else:
            conn.rollback()
            print("!!!!!!!!!!!!!!!!!!!!!!Exception!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

# Heading
header = Frame(statement,width=2000,height= 150,bg='yellow',bd=5,relief="raised")
header.pack(side="top",fill=BOTH)
# Label for Header
label_1 = Label(header,text="PUNJAB NATIONAL BANK",font=('arial',28,'bold'),height= 1,justify="center",fg="black",bg="yellow")
label_1.pack(side="top",ipadx=5,ipady=5)


# Body Frame
body = Frame(statement,width=450,height= 150,bg='yellow',bd=5,relief="raised")
body.pack(side="bottom",expand=True)

# Account Number
Account = Label(body, text="Enter Account no",font=('arial',12,'bold'),bg='yellow')
Account.place(x=35,y=30)
account = StringVar()

# Textbox for Account Number
tb1=Entry(body,font=('arial',12,'bold'),textvariable=account)
tb1.place(x=225,y=30)

# Mini Statement Show Button
Button_1 = Button(body, text="Show Statement",font=('arial',12,'bold'), width=13,bd=5,height=1,padx=2,pady=2,relief="raised",command=Statement)
Button_1.place(x=130,y=75)
statement.mainloop()
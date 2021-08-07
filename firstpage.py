from tkinter import *
from pymysql import *
import os
 

firstpage = Tk()
firstpage.title("Punjab National Bank")
firstpage.geometry("852x480")
firstpage.config(bg="Aqua") 

def login():
    os.system("E:\PROGRAMS\Python\PythonProject\loginpage.py")

def create():
    os.system("E:\PROGRAMS\Python\PythonProject\Account_creation.py")

# Heading 'Punjab National Bank'
header = Frame(firstpage,width=2000,height= 150,bg='yellow',bd=5,relief="raised")
header.pack(side="top",fill=BOTH)

# Label for Header
label_1 = Label(header,text="PUNJAB NATIONAL BANK",font=('arial',28,'bold'),height= 1,justify="center",fg="black",bg='yellow')
label_1.pack(side="top",ipadx=5,ipady=5)


# Body Frame
body = Frame(firstpage,width=380,height= 150,bg='yellow',bd=5,relief="raised")
body.pack(side="bottom",expand=True)
label_2 = Label(body,text="You want to ",font=('Arial',14,'bold'),bg='yellow')
label_2.place(x=125,y=25)

Button_1 = Button(body, text="Login",font=('arial',12,'bold'), width=10,bd=4,height=1,relief="raised",command=login)
Button_1.place(x=35,y=65)

Button_1 = Button(body, text="Create Account",font=('arial',12,'bold'), width=14,bd=4,height=1,relief="raised",command=create)
Button_1.place(x=180,y=65)
firstpage.mainloop()

#Login Form
from tkinter import *
root = Tk()
root.geometry("400x400")
root.resizable(0,0)
l1 = Label(root,text="Enter User Name :",font=("Airal",20))
l1.grid(row=0,column=0)

e1 = Entry(root,font=("Airal",20), fg="blue",bg="pink",width="10")
e1.grid(row=0,column=1,pady=25,sticky=W)

l2 = Label(root,text="Enter PassWord :", font=("Airal",20))
l2.grid(row=1,column=0,sticky=W)

e2 = Entry(root,font=("Airal",20),fg="blue",bg="pink", width="10",show="*")
e2.grid(row=1,column=1,pady=25,sticky=W)

b1 = Button(root,text="Login",font=("Airal",20))
b1.grid(row=2,column=0,columnspan=2)
root.mainloop()
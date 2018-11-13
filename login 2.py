from tkinter import *

root = Tk()
root.geometry('500x500')
root.title("Player Form")

L0 = Label(root, text="Player Form",width=20,font=("bold", 20))
L0.place(x=90,y=53)
L1=Label(root, text="FullName",width=20,font=("bold", 10))
L1.place(x=80,y=130)

e2 = Entry(root)
e2.place(x=240,y=130)

L3 = Label(root, text="Email",width=20,font=("bold", 10))
L3.place(x=68,y=180)

e4 = Entry(root)
e4.place(x=240,y=180)

L5 = Label(root, text="Gender",width=20,font=("bold", 10))
L5.place(x=70,y=230)
var = IntVar()
Radiobutton(root,text="Male",padx=5,variable=var,value=1).place(x=235,y=230)
Radiobutton(root, text="Female",padx=20,variable=var,value=2).place(x=290,y=230)

L6=Label(root,text="country",width=20,font=("bold", 10))
L6.place(x=70,y=280)

list1 = ['Canada','India','UK','Nepal','Iceland','South Africa'];
c=StringVar()
droplist=OptionMenu(root,c, *list1)
droplist.config(width=15)
c.set('select your country') 
droplist.place(x=240,y=280)

L7=Label(root,text="Programming",width=20,font=("bold", 10))
L7.place(x=85,y=330)
var1 = IntVar()
Checkbutton(root, text="C++",variable=var1).place(x=235,y=330)
var2 = IntVar()
Checkbutton(root,text="python",variable=var2).place(x=290,y=330)

Button(root,text='Submit',width=20,bg='brown',fg='white').place(x=180,y=380)

root.mainloop()

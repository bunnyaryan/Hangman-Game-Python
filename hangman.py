from tkinter import *
import random
from tkinter import messagebox


root = Tk()
NAME = StringVar()


def login():
    
    root.geometry('500x500')
    root.title("Player Form")

    L0 = Label(root, text="Player Form",width=20,font=("bold", 20))
    L0.place(x=90,y=53)
    L1=Label(root, text="FullName",width=20,font=("bold", 10))
    L1.place(x=80,y=130)
    L1.focus()

    #name = StringVar()
    e2 = Entry(root, textvariable=NAME)
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


    Button(root,text='Submit',width=20,bg='brown',fg='white', command=lambda: hangman(NAME)).place(x=180,y=380)

    root.mainloop()


def hangman(name):
    window=Tk()

    window.title("Hang-Man Game")
    window.geometry("650x700+320+80")

    
    p1=PhotoImage(master=window, file="as1.PNG")
    p2=PhotoImage(master=window, file="as2.PNG")
    p3=PhotoImage(master=window, file="as3.PNG")
    p4=PhotoImage(master=window, file="as4.PNG")
    p5=PhotoImage(master=window, file="as5.PNG")
    print(p3)
    tup1=(p1,p2,p3,p4,p5)
    tup2=('parrot','cub','hen','owl','monkey')
    letters=list()
    def data(letter):
        letters.append(letter)
        res = e1.get() + '*'
        e1.delete('0', END)
        e1.insert(INSERT, res)

        
    def word():
        
        print(''.join(letters))
        if (tup2[n]==str(''.join(letters))):
            messagebox.showinfo('Congratulations','You won the game !')
        
        else:
           nog(1)
           messagebox.showerror('Failed','You lost game !')    
           del letters[:]
           
    def refresh():
        global n
        n=random.randint(0,len(tup1)-1)
        l1=Label(window,image=tup1[n],height=300,width=300)
        l1.place(x=10,y=10)
        del letters[:]
        e1.delete('0', END)

    l3=Label(window,text='Player name',font='Times,16,Bold')
    l3.place(x=380,y=30)
    e3=Entry(window,bd=2,width=20)
    e3.insert(INSERT, NAME.get())
    e3.place(x=510,y=35)

    b=Button(window,text="New word",bg='brown',fg='white',relief="ridge",command=refresh)
    b.place(x=400,y=100)


    e1=Entry(window,bd=2)
    e1.place(x=400,y=140)
    e1.focus()
    refresh()
    b27=Button(window,text='Submit',bg='brown',fg='white',command=word)
    b27.place(x=400,y=180)
    b1=Button(window,text="A",bg="Light Blue",font='Times 14 bold',command=lambda: data('a'))
    b2=Button(window,text="B",bg="Light Blue",font='Times 14 bold',command=lambda: data('b'))
    b3=Button(window,text="C",bg="Light Blue",font='Times 14 bold',command=lambda: data('c'))
    b4=Button(window,text="D",bg="Light Blue",font='Times 14 bold',command=lambda: data('d'))
    b5=Button(window,text="E",bg="Light Blue",font='Times 14 bold',command=lambda: data('e'))
    b6=Button(window,text="F",bg="Light Blue",font='Times 14 bold',command=lambda: data('f'))
    b7=Button(window,text="G",bg="Light Blue",font='Times 14 bold',command=lambda: data('g'))
    b8=Button(window,text="H",bg="Light Blue",font='Times 14 bold',command=lambda: data('h'))
    b9=Button(window,text="I",bg="Light Blue",font='Times 14 bold',command=lambda: data('i'))
    b10=Button(window,text="J",bg="Light Blue",font='Times 14 bold',command=lambda: data('j'))
    b11=Button(window,text="K",bg="Light Blue",font='Times 14 bold',command=lambda: data('k'))
    b12=Button(window,text="L",bg="Light Blue",font='Times 14 bold',command=lambda: data('l'))
    b13=Button(window,text="M",bg="Light Blue",font='Times 14 bold',command=lambda: data('m'))
    b14=Button(window,text="N",bg="Light Blue",font='Times 14 bold',command=lambda: data('n'))
    b15=Button(window,text="O",bg="Light Blue",font='Times 14 bold',command=lambda: data('o'))
    b16=Button(window,text="P",bg="Light Blue",font='Times 14 bold',command=lambda: data('p'))
    b17=Button(window,text="Q",bg="Light Blue",font='Times 14 bold',command=lambda: data('q'))
    b18=Button(window,text="R",bg="Light Blue",font='Times 14 bold',command=lambda: data('r'))
    b19=Button(window,text="S",bg="Light Blue",font='Times 14 bold',command=lambda: data('s'))
    b20=Button(window,text="T",bg="Light Blue",font='Times 14 bold',command=lambda: data('t'))
    b21=Button(window,text="U",bg="Light Blue",font='Times 14 bold',command=lambda: data('u'))
    b22=Button(window,text="V",bg="Light Blue",font='Times 14 bold',command=lambda: data('v'))
    b23=Button(window,text="W",bg="Light Blue",font='Times 14 bold',command=lambda: data('w'))
    b24=Button(window,text="X",bg="Light Blue",font='Times 14 bold',command=lambda: data('x'))
    b25=Button(window,text="Y",bg="Light Blue",font='Times 14 bold',command=lambda: data('y'))
    b26=Button(window,text="Z",bg="Light Blue",font='Times 14 bold',command=lambda: data('z'))
    #b1.place(bordermode=OUTSIDE, height=98, width=70,x=20,y=330)
    b1.place(x=10,y=330)
    b2.place(x=50,y=330)
    b3.place(x=90,y=330)
    b4.place(x=130,y=330)
    b5.place(x=170,y=330)
    b6.place(x=210,y=330)
    b7.place(x=250,y=330)
    b8.place(x=290,y=330)
    b9.place(x=330,y=330)
    b10.place(x=370,y=330)
    b11.place(x=410,y=330)
    b12.place(x=450,y=330)
    b13.place(x=490,y=330)
    b14.place(x=530,y=330)
    b15.place(x=570,y=330)
    b16.place(x=30,y=370)
    b17.place(x=70,y=370)
    b18.place(x=110,y=370)
    b19.place(x=150,y=370)
    b20.place(x=190,y=370)
    b21.place(x=230,y=370)
    b22.place(x=270,y=370)
    b23.place(x=310,y=370)
    b24.place(x=350,y=370)
    b25.place(x=390,y=370)
    b26.place(x=430,y=370)

    l2=Label(window,text='No. of Guesses remaining :',font='Times,16,Bold')
    l2.place(x=20,y=450)

    def nog(x):
        v = StringVar(window, value=x)
        e2= Entry(window, textvariable=v,font='Times,16,Bold')
        e2.place(x=270,y=455)
    nog(2)
    window.mainloop()
login()

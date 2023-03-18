#Libraries
from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
import ast

#Application Setup
root = Toplevel()
root.title("Database Login")
root.configure(bg="white")
root.geometry("925x500+300+200")
root.resizable(False,False)

#Functions
def on_enter1(event):
    user.delete(0,'end')

def on_enter2(event):
    password.delete(0,'end')
    password.config(show="*")

def on_leave1(event):
    a = user.get()
    if(a==''): 
        user.insert(0,"Username")

def on_leave2(event):
    b = password.get()
    if(b==''):
        password.insert(0,"Password")
        password.config(show='')

def sign_in():
    Username = user.get()
    Password = password.get()

    file = open('datasheet.txt')
    d = file.read()
    r = ast.literal_eval(d)
    file.close()

    if(Username=='Username' and Password=='Password'):
        messagebox.showwarning("Blank Input","Please enter username and password")
    elif(Username in r.keys() and Password==r[Username]):
        messagebox.showinfo("Login Success","You have logged in successfully")
        import Steganography
    elif(Username!="harsh"): messagebox.showerror("Error","Invalid username")
    elif(Password!="h1234"): messagebox.showerror("Error","Invalid password")
    else:
        messagebox.showerror("Invalid Input","Invalid username and password")

def signup():
    root.destroy
    import DatabaseSignup

def show():
    password.config(show='')

#Application Creation
img1 = PhotoImage(file="E:\\build app with python\\Database Setup\\database login logo.png")
img2 = PhotoImage(file="E:\\build app with python\\Database Setup\\login person.png")
root.iconphoto(False,img1)
l1 = Label(root,image=img2,bg="white") ; l1.place(x=50,y=50)

f1 = Frame(root,width=350,height=350,bg="white") ; f1.place(x=480,y=70)

head = Label(f1,text="Sign In",fg="#57a1f8",bg="white",font=('Microsoft',23,'bold'))
head.place(x=100,y=5) 

user = Entry(f1,width=25,fg="black",bd=0,bg="white",font=("Microsoft",12),relief=RAISED) ; user.insert(0,"Username"); user.bind('<FocusIn>',on_enter1);
user.bind('<FocusOut>',on_leave1) ; user.place(x=30,y=80)

password = Entry(f1,width=25,fg="black",bd=0,bg="white",
font=("Microsoft",12),relief=RAISED) ; password.insert(0,"Password")
password.bind('<FocusIn>',on_enter2); password.bind('<FocusOut>',on_leave2)
password.place(x=30,y=150);

f2 = Frame(root,width=295,height=2,bg="black").place(x=510,y=180)
f3 = Frame(root,width=295,height=2,bg="black").place(x=510,y=250)

btn1 = Button(f1,text="Sign In",bg="#57a1f8",fg="black",bd=2,cursor="hand2"
,activebackground="#57a1f8",activeforeground="black",
width=39,pady=7,relief=RAISED,command=sign_in)
btn1.place(x=35,y=208)

btn2 = Button(f1,text="Show",bd=0,fg="#57a1f8",bg="white",cursor="hand2",
activebackground="white",activeforeground="#57a1f8",command=show)
btn2.place(x=290,y=150)

l2 = Label(f1,text="Don't have an account?",fg="black",bg="white",
font=("Microsoft",9,"bold")) ; l2.place(x=75,y=270)

sign_up = Button(f1,text="Sign up",width=6,bg="white",fg="#57a1f8",bd=0,cursor="hand2",
font=Font(size=9,weight="bold"),activebackground="white",command=signup)
sign_up.place(x=215,y=270)

root.mainloop()
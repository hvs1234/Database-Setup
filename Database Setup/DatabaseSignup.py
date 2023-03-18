#Libraries
from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
import ast

#Application Setup
root = Toplevel()
root.title("Database Sign Up")
root.configure(bg="white")
root.geometry("925x500+300+200")
root.resizable(False,False)

#Functions
def on_enter1(event):
    user.delete(0,'end')

def on_enter2(event):
    password.delete(0,'end')

def on_enter3(event):
    new_password.delete(0,'end')

def on_leave1(event):
    a = user.get()
    if(a==''): 
        user.insert(0,"Create Username")

def on_leave2(event):
    b = password.get()
    if(b==''):
        password.insert(0,"Create Password")

def on_leave3(event):
    c = new_password.get()
    if(c==''): 
        new_password.insert(0,"Confirm Password")

def sign_up():
    Username = user.get()
    Password = password.get()
    New_Password = new_password.get()

    if(Username=='' and Password=='' and New_Password==''):
        messagebox.showwarning("Blank Sign up","Please fill input here")
    if(Password==New_Password):
        try:
            file = open('datasheet.txt','r+')
            d = file.read()
            r=ast.literal_eval(d)

            dict1 = {Username:Password}
            r.update(dict1) ; file.truncate(0) ; file.close()

            file = open('datasheet.txt','w')
            w = file.write(str(r))

            messagebox.showinfo("Signup Success","You have signed up successfully")
        except:
            file = open('datasheet.txt','w')
            p = str({'Username':'Password'})
            file.write(p) ; file.close()
    
    else:
        messagebox.showerror("Invalid Match","Password doesn't match")

def hide():
    password.config(show="*")
    new_password.config(show="*")

def show():
    password.config(show='')
    new_password.config(show='')

def signin():
    import DatabaseLogin

#Application Creation
img1 = PhotoImage(file="E:\\build app with python\\Database Setup\\database login logo.png")
img2 = PhotoImage(file="E:\\build app with python\\Database Setup\\signup.png")
root.iconphoto(False,img1)
l1 = Label(root,image=img2,bg="white") ; l1.place(x=50,y=120)

f1 = Frame(root,width=350,height=750,bg="white") ; f1.place(x=480,y=70)

head = Label(f1,text="Sign Up",fg="#57a1f8",bg="white",font=('Microsoft',23,'bold'))
head.place(x=100,y=5) 

user = Entry(f1,width=25,fg="black",bd=0,bg="white",font=("Microsoft",12),relief=RAISED) ; user.insert(0,"Create Username"); user.bind('<FocusIn>',on_enter1);
user.bind('<FocusOut>',on_leave1) ; user.place(x=30,y=80)

password = Entry(f1,width=25,fg="black",bd=0,bg="white",font=("Microsoft",12),relief=RAISED) ; password.insert(0,"Create Password") ; password.bind('<FocusIn>',on_enter2);
password.bind('<FocusOut>',on_leave2) ; password.place(x=30,y=150)

new_password = Entry(f1,width=25,fg="black",bd=0,bg="white",font=("Microsoft",12),relief=RAISED) ; new_password.insert(0,"Confirm Password") ; 
new_password.bind('<FocusIn>',on_enter3); new_password.bind('<FocusOut>',on_leave3)
new_password.place(x=30,y=220)

f2 = Frame(root,width=295,height=2,bg="black").place(x=510,y=180)
f3 = Frame(root,width=295,height=2,bg="black").place(x=510,y=250)
f4 = Frame(root,width=295,height=2,bg="black").place(x=510,y=320)

btn1 = Button(f1,text="Sign Up",bg="#57a1f8",fg="black",bd=2,cursor="hand2"
,activebackground="#57a1f8",activeforeground="black",
width=39,pady=7,relief=RAISED,command=sign_up)
btn1.place(x=35,y=280)

btn2 = Button(f1,text="Hide",bd=0,fg="#57a1f8",bg="white",cursor="hand2",
activebackground="white",activeforeground="#57a1f8",command=hide)
btn2.place(x=290,y=150)
btn3 = Button(f1,text="Show",bd=0,fg="#57a1f8",bg="white",cursor="hand2",
activebackground="white",activeforeground="#57a1f8",command=show)
btn3.place(x=290,y=220)

l2 = Label(f1,text="Already have an account?",fg="black",bg="white",
font=("Microsoft",9,"bold")) ; l2.place(x=75,y=340)

sign_up = Button(f1,text="Sign in",width=6,bg="white",fg="#57a1f8",bd=0,cursor="hand2",
font=Font(size=9,weight="bold"),activebackground="white",command=signin)
sign_up.place(x=225,y=340)

root.mainloop()
from tkinter import *
from tkinter import Text,Tk
import os
import sqlite3
from tkinter import ttk, messagebox
import tkinter as tk

#________________________________________

def signup():


            winsignup = Tk()
            winsignup.title("sign up")
            winsignup.maxsize(width=500,height=600)
            winsignup.minsize(width=500,height=600)


            #heading
            heading=Label(winsignup,text="signup",font="Verdana 20 bold")
            heading.place(x=80,y=60)

            first_name=Label(winsignup,text="First name",font="Verdana 10 bold")
            first_name.place(x=80,y=130)

            last_name = Label(winsignup, text= "Last Name :" , font='Verdana 10 bold')
            last_name.place(x=80,y=160)

            age = Label(winsignup, text= "Age :" , font='Verdana 10 bold')
            age.place(x=80,y=190)

            Gender = Label(winsignup, text= "Gender :" , font='Verdana 10 bold')
            Gender.place(x=80,y=220)    

            city = Label(winsignup, text= "City :" , font='Verdana 10 bold')
            city.place(x=80,y=260)

            add = Label(winsignup, text= "Address :" , font='Verdana 10 bold')
            add.place(x=80,y=290)

            user_name = Label(winsignup, text= "User Name :" , font='Verdana 10 bold')
            user_name.place(x=80,y=320)

            password = Label(winsignup, text= "Password :" , font='Verdana 10 bold')
            password.place(x=80,y=350)

            very_pass = Label(winsignup, text= "Verify Password:" , font='Verdana 10 bold')
            very_pass.place(x=80,y=380)

# Entry Box ------------------------------------------------

            first_name = StringVar()
            last_name = StringVar()
            age = IntVar(winsignup, value='0')
            var= StringVar()
            city= StringVar()
            add = StringVar()
            user_name = StringVar()
            password = StringVar()
            very_pass = StringVar()
        
        

	
            first_name = Entry(winsignup, width=40 , textvariable = first_name)
            first_name.place(x=200 , y=133)


	
            last_name = Entry(winsignup, width=40 , textvariable = last_name)
            last_name.place(x=200 , y=163)

            age = Entry(winsignup, width=40, textvariable=age)
            age.place(x=200 , y=193)

	
    
            var= ttk.Combobox(winsignup, width=30, textvariable= var, state='readonly')
            var['values']=('Male','Female','Transgender')
            var.current()
            var.place(x=200,y=220)

            city = Entry(winsignup, width=40,textvariable = city)
            city.place(x=200 , y=263)


            add = Entry(winsignup, width=40 , textvariable = add)
            add.place(x=200 , y=293)

	
            user_name = Entry(winsignup, width=40,textvariable = user_name)
            user_name.place(x=200 , y=323)

            password = Entry(winsignup, width=40, textvariable = password)
            password.place(x=200 , y=353)

	
            very_pass= Entry(winsignup, width=40 ,show="*" , textvariable = very_pass)
            very_pass.place(x=200 , y=383)


# button login and clear

            btn_signup = Button(winsignup, text = "Signup" ,font='Verdana 10 bold')
            btn_signup.place(x=200,y=413)
            

	


            

            

    

win =Tk()
win.title("hospital mangement")

win.maxsize(width=500,height=500)
win.minsize(width=500,height=500)

Label(text="Hospital mangement",bg="light blue",width="300",height="4",font=("calibri",16,"bold")).pack()
Label(win,text="").pack()

heading= Label(win,text="login",font='Verdana 25 bold')
heading.place(x=80 , y=150)

username =Label(win,text="User name",font='Verdana 10 bold')
username.place(x=80 ,y =220)

userpass=Label(win,text="Password",font='Verdana 10 bold')
userpass.place(x=80 ,y = 260)

#entry box

user_name =StringVar()
password =StringVar()

userentry =Entry(win,width=40,textvariable=user_name)
userentry.focus()
userentry.place(x=200,y=223)

passentry =Entry(win,width=40,show="*",textvariable=password)
passentry.place(x=200,y=260)

btn_login =Button(win,text="Login",font='Verdana 10 bold')
btn_login.place(x=200,y=293)

sign_up_btn= Button(win,text="register",command=signup)
sign_up_btn.place (x=420,y=70)

win.mainloop

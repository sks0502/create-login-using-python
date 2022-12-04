from tkinter import *
from tkinter import Text,Tk
import os
import sqlite3
from tkinter import ttk, messagebox
import tkinter as tk

#________________________________________



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

win.mainloop

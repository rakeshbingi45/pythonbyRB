import tkinter as tk
import pickle

def click(): 
    username=un.get()
    password=pw.get()
    dbfile=open("form","rb")
    t = pickle.load(dbfile)
    if username in t and t[username]==password:
        lb4["text"]="Logged In"
    else:
        lb4["text"]="Login Failed"

win=tk.Tk()
win.title="Login Form"

lb1=tk.Label(win,text="Login Form")
lb2=tk.Label(win,text="Username")
un=tk.Entry(win)
lb3=tk.Label(win,text="Password")
pw=tk.Entry(win,show="*")
button=tk.Button(win,text="Login",command=click)
lb4=tk.Label(win,text="")

lb1.pack()
lb2.pack()
un.pack()
lb3.pack()
pw.pack()
button.pack()
lb4.pack()

win.mainloop()
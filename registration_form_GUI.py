import tkinter as tk
import pickle

def click(): 
    username=un.get()
    password=pw.get()
    try:
        dbfile=open("form","rb")
        db=pickle.load(dbfile)
        dbfile.close()
        db[username]=password
        dbfile=open("form","wb")
        pickle.dump(db,dbfile)
        dbfile.close()
        lb4["text"]="Successfully Registered"
    except FileNotFoundError:
        db={}
        db[username]=password
        dbfile=open("form","wb")
        pickle.dump(db,dbfile)
        dbfile.close()
        lb4["text"]="Successfully Registered"
    dbfile=open("form","rb")
    db=pickle.load(dbfile)
    print(db)
    dbfile.close()
    
win=tk.Tk()
win.title="Registration Form"

lb1=tk.Label(win,text="Registration Form")
lb2=tk.Label(win,text="Username")
un=tk.Entry(win)
lb3=tk.Label(win,text="Password")
pw=tk.Entry(win,show="*")
button=tk.Button(win,text="Register",command=click)
lb4=tk.Label(win,text="")

lb1.pack()
lb2.pack()
un.pack()
lb3.pack()
pw.pack()
button.pack()
lb4.pack()

win.mainloop()
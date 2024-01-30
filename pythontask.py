import tkinter as tk
from tkinter import messagebox as mb
import pickle
from tkinter import *

def loadData():
    try:
        dbfile=open("libbook","rb")
        db=pickle.load(dbfile)
        dbfile.close()
        return db
    except FileNotFoundError:
        li=[]
        return li 
      
dbl=loadData()

def savedata():
    dbfile = open('libbook', 'wb')     
    pickle.dump(dbl, dbfile)
    dbfile.close()
    
def add():
    def add_cancelcmd():
        add.destroy()
    def add_okcmd():
        dictionary={
            "isbn":add_isbn_ent.get(),"bname":add_title_ent.get(),"aname": add_author_ent.get()
        }
        dbl.append(dictionary)
        savedata()
        view_all()
        add.destroy()
        mb.showinfo("Add","Added Successfully")
    add= tk.Toplevel(window)
    add_title=tk.Label(add,text="Title:")
    add_isbn=tk.Label(add,text="ISBN:")
    add_author=tk.Label(add,text="Author:")
    add_title_ent=tk.Entry(add)
    add_isbn_ent=tk.Entry(add)
    add_author_ent=tk.Entry(add)
    add_ok=tk.Button(add,text="Add",command=add_okcmd)
    add_cancel=tk.Button(add,text="Cancel",command=add_cancelcmd)    

    add_title.place(relx=0.1,rely=0.1)
    add_title_ent.place(relx=0.35,rely=0.1)
    add_author.place(relx=0.1,rely=0.3)
    add_author_ent.place(relx=0.35,rely=0.3)
    add_isbn.place(relx=0.1,rely=0.5)
    add_isbn_ent.place(relx=0.35,rely=0.5)
    add_ok.place(relx=0.2,rely=0.7)
    add_cancel.place(relx=0.6,rely=0.7)
    add.mainloop()

def update_book():
    def upd_cancelcmd():
        upd.destroy()
    def upd_updatecmd():
        a11=upd_isbn_ent.get()
        a22=upd_title_ent.get()
        a33=upd_author_ent.get()
        d=0
        for j in dbl:
            if int(j["isbn"]) == a1: 
                print("match found")
                break
            d=d+1
        dbl[d]={"isbn":a11,"bname":a22,"aname":a33}
        savedata()
        clear_lb()
        view_all()
        upd.destroy()
        mb.showinfo("Update","Updated Successfully")
    upd=tk.Toplevel(window)
    upd_title=tk.Label(upd,text="Title:")
    upd_isbn=tk.Label(upd,text="ISBN:")
    upd_author=tk.Label(upd,text="Author:")
    upd_title_ent=tk.Entry(upd)
    upd_isbn_ent=tk.Entry(upd)
    upd_author_ent=tk.Entry(upd)
    for i in book_list.curselection():
        a=book_list.get(i)
        print(a)
        b=a.split(" - ")
        print(b)
        a1=int(b[0])
        upd_isbn_ent.insert(0,a1)
        a2=str(b[1]) 
        upd_title_ent.insert(0,a2)  
        a3=str(b[2])
        upd_author_ent.insert(0,a3)
    upd_ok=tk.Button(upd,text="Update",command=upd_updatecmd)
    upd_cancel=tk.Button(upd,text="Cancel",command=upd_cancelcmd)    

    upd_title.place(relx=0.1,rely=0.1)
    upd_title_ent.place(relx=0.35,rely=0.1)
    upd_author.place(relx=0.1,rely=0.3)
    upd_author_ent.place(relx=0.35,rely=0.3)
    upd_isbn.place(relx=0.1,rely=0.5)
    upd_isbn_ent.place(relx=0.35,rely=0.5)
    upd_ok.place(relx=0.2,rely=0.7)
    upd_cancel.place(relx=0.6,rely=0.7)
    upd.mainloop()

def delete_book():
    for i in book_list.curselection():
        dbl.pop(i)
        savedata()
        view_all()
    mb.showinfo("Delete","Deleted Successfully")
    
def clear_lb():
    book_list.delete(0,tk.END)

def search():
    clear_lb()
    t = title_entry.get()
    isbn = isbn_entry.get()
    a = author_entry.get()
    c=0
    for i in dbl:
        if str(i["isbn"]) == isbn or str(i["bname"]) == t or str(i["aname"]) == a:
            st = str(i["isbn"])+" - "+i["bname"]+" - "+" by "+i["aname"]
            book_list.insert(c,st)
            c+=1

def view_all():
    clear_lb()
    isbn_entry.delete(0,tk.END)
    title_entry.delete(0,tk.END)
    author_entry.delete(0,tk.END)
    c=0
    for i in dbl:
        st = str(i["isbn"])+" - "+i["bname"]+" - "+" by "+i["aname"]
        book_list.insert(c,st)
        c+=1

def close():
    exit()

window=tk.Tk() 
window.title("Library Book Management")
window.geometry("550x450")

title=tk.Label(window,text="Title:")
title_entry=tk.Entry(window)
isbn=tk.Label(window,text="ISBN:")
isbn_entry=tk.Entry(window)
author=tk.Label(window,text="Author:")
author_entry=tk.Entry(window)

book_list=tk.Listbox(window,width=53,height=24)

view_allbtn=tk.Button(window,text="View all",width=28,command=view_all)
search_entry=tk.Button(window,text="Search Entry",width=28,command=search)
add_entry=tk.Button(window,text="Add Entry",width=28,command=add)
update_selected=tk.Button(window,text="Update Selected",width=28,command=update_book)
delete_selected=tk.Button(window,text="Delete Selected",width=28,command=delete_book)
closebtn=tk.Button(window,text="Close",width=28,command=close)

title.place(relx=0.01,rely=0)
title_entry.place(relx=0.07,rely=0)
isbn.place(relx=0.01,rely=0.06)
isbn_entry.place(relx=0.07,rely=0.06)
author.place(relx=0.6,rely=0)
author_entry.place(relx=0.7,rely=0)

book_list.place(relx=0,rely=0.12)

view_allbtn.place(relx=0.6,rely=0.15)
search_entry.place(relx=0.6,rely=0.30)
add_entry.place(relx=0.6,rely=0.45)
update_selected.place(relx=0.6,rely=0.60)
delete_selected.place(relx=0.6,rely=0.75)
closebtn.place(relx=0.6,rely=0.90)
view_all()
window.mainloop()
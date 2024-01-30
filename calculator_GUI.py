import tkinter as tk

def click(number):
    current=en.get()
    en.delete(0,tk.END)
    en.insert(0,str(current)+str(number))

def button_add():
    first_number=en.get()
    global f_num
    global math
    math ="addition"
    f_num=int(first_number)
    en.delete(0,tk.END)

def button_sub():
    first_number=en.get()
    global f_num
    global math
    math ="subtraction"
    f_num=int(first_number)
    en.delete(0,tk.END)

def button_mul():
    first_number=en.get()
    global f_num
    global math
    math ="multiplication"
    f_num=int(first_number)
    en.delete(0,tk.END)

def button_div():
    first_number=en.get()
    global f_num
    global math
    math ="division"
    f_num=int(first_number)
    en.delete(0,tk.END)

def button_cal():
    second_number=en.get()
    s_num=int(second_number)
    en.delete(0,tk.END)
    if math =="addition":
        en.insert(0, f_num+s_num)
    elif math =="subtraction":
        en.insert(0, f_num-s_num)
    elif math =="multiplication":
        en.insert(0, f_num*s_num)
    elif math =="division":
        en.insert(0, f_num/s_num)  
    else:
        pass  

def clear():
    en.delete(0,tk.END)

win = tk.Tk()
win.title("Calculator")

en = tk.Entry(win,width=49)

button_1 = tk.Button(win,text = "1", padx=20,pady=20, bg='white',command=lambda:click(1))
button_2 = tk.Button(win,text = "2", padx=20,pady=20, bg='white',command=lambda:click(2))
button_3 = tk.Button(win,text = "3", padx=20,pady=20, bg='white',command=lambda:click(3))
button_4 = tk.Button(win,text = "4", padx=20,pady=20, bg='white',command=lambda:click(4))
button_5 = tk.Button(win,text = "5", padx=20,pady=20, bg='white',command=lambda:click(5))
button_6 = tk.Button(win,text = "6", padx=20,pady=20, bg='white',command=lambda:click(6))
button_7 = tk.Button(win,text = "7", padx=20,pady=20, bg='white',command=lambda:click(7))
button_8 = tk.Button(win,text = "8", padx=20,pady=20, bg='white',command=lambda:click(8))
button_9 = tk.Button(win,text = "9", padx=20,pady=20, bg='white',command=lambda:click(9))
button_0 = tk.Button(win,text = "0", padx=47.5,pady=20, bg='white',command=lambda:click(0))
button_add = tk.Button(win,text = "+", padx=20,pady=20, bg='white',command=button_add)
button_sub = tk.Button(win,text = "-", padx=20,pady=20, bg='white',command=button_sub)
button_mul = tk.Button(win,text = "*", padx=20,pady=20, bg='white',command=button_mul)
button_div = tk.Button(win,text = "/", padx=20,pady=20, bg='white',command=button_div)
button_cal = tk.Button(win,text = "=",padx=20,pady=20, bg='white', command=button_cal)
button_clear= tk.Button(win,text = "CLEAR",padx=20,pady=115,activebackground='red',activeforeground='blue',bg='white', command=clear)


en.grid(row=0,column=0,columnspan=5)
button_1.grid(row=1,column=0)
button_2.grid(row=1,column=1)
button_3.grid(row=1,column=2)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_7.grid(row=3,column=0)
button_8.grid(row=3,column=1)
button_9.grid(row=3,column=2)
button_0.grid(row=4,column=0,columnspan=2)
button_add.grid(row=1,column=3)
button_sub.grid(row=2,column=3)
button_mul.grid(row=3,column=3)
button_div.grid(row=4,column=3)
button_cal.grid(row=4,column=2)
button_clear.grid(row=1,column=4,rowspan=5)

win.mainloop()
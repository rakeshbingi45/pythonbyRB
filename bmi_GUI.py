import tkinter as tk

def click():
    h=float(entry1.get())
    w=float(entry2.get())
    bmif=w/(h*h)
    print(bmif)
    bmi="{:.2f}".format(bmif)
    if bmif<16:
        label4["text"]="Your BMI is " + format(bmi) + " kg/m\u00b2 \n and You fall under Severe Thinness Category"
    elif bmif>16 and bmif<17:
        label4["text"]="Your BMI is " + format(bmi) + " kg/m\u00b2 \n and You fall under Moderate Thinness Category"
    elif bmif>17 and bmif<18.5:
        label4["text"]="Your BMI is " + format(bmi) + " kg/m\u00b2 \n and You fall under Mild Thinness Category"
    elif bmif>18.5 and bmif<25:
        label4["text"]="Your BMI is " + format(bmi) + " kg/m\u00b2 \n and You fall under Normal Category"
    elif bmif>25 and bmif<30:
        label4["text"]="Your BMI is " + format(bmi) + " kg/m\u00b2 \n and You fall under Overweight Category"
    elif bmif>30 and bmif<35:
        label4["text"]="Your BMI is " + format(bmi) + " kg/m\u00b2 \n and You fall under Obese Class I Category"
    elif bmif>35 and bmif<40:
        label4["text"]="Your BMI is " + format(bmi) + " kg/m\u00b2 \n and You fall under Obese Class II Category"
    elif bmif>40:
        label4["text"]="Your BMI is " + format(bmi) + " kg/m\u00b2 \n and You fall under Obese Class III Category"
    else:
        label4["text"]="Error"

win=tk.Tk()
win.title("BMI Calculator")
win.geometry("250x168")

label1= tk.Label(win,text="BMI Calculator")
label2= tk.Label(win,text="Enter your Height (m)")
entry1= tk.Entry(win)
label3= tk.Label(win,text="Enter your Weight (kg)")
entry2= tk.Entry(win)
button= tk.Button(win,text="Calculate",command=click)
label4= tk.Label(win,text=" ")

label1.pack()
label2.pack()
entry1.pack()
label3.pack()
entry2.pack()
button.pack()
label4.pack()

win.mainloop()
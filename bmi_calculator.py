from tkinter import *


root = Tk()
root.title("BMI Calculator")
root.configure(width=100, height=100)
root.configure(bg="black")


def calc():
    BMI = BMI_val(mass.get(), height.get())
    Stat = getStatus()
    stat.set(Stat)
    bmi_val.set(format(BMI, ".2f"))


def BMI_val(mass, height):
    return mass/height ** 2


def getHeight():
    return height


def clear():
    stat.set("")
    bmi_val.set("0.0")
    mas.delete(0, "end")
    heigh.delete(0, "end")


def getWidth():
    return mass


def getStatus():
    if bmi_val.get() > 40:
        return "You are Obbess Class 3"
    elif bmi_val.get() > 35 or bmi_val.get() < 40:
        return "You are Obess Class 2"
    elif bmi_val.get() > 30 or bmi_val.get() < 35:
        return "You are Obess Class 1"
    elif bmi_val.get() > 25 or bmi_val.get() < 30:
        return "You are overweight"
    elif bmi_val.get() > 18.5 or bmi_val.get() < 25:
        return "You are normal"
    elif bmi_val.get() > 17 or bmi_val.get() < 18.5:
        return "You are on the mild scale"
    else:
        return "You are moderately thin"

height = DoubleVar()
h_label = Label(root, text="Height", fg="red", bg="black",
                font=("Calibri 14 bold"), pady=5, padx=8)

heigh = Entry(root, textvariable=height)
h_label.grid(row=2)
heigh.grid(row=2, column=1, columnspan=2, padx=5)

mass = DoubleVar()
w_label = Label(root, text="Mass", fg="red", bg="black",
                font=("Calibri 14 bold"), pady=10, padx=2)

mas = Entry(root, textvariable=mass)
w_label.grid(row=4)
mas.grid(row=4, column=1)

bmi_val = DoubleVar()
stat = StringVar()
bmi = Label(root, text="BMI: ", fg="blue", bg="black",
            font=("Calibri 14 bold"), padx=2, pady=10, justify=LEFT)

status = Label(root, text="Status", fg="blue", bg="black",
               font=("Calibri 14 bold"), padx=2, pady=10)

status_msg = Label(root, textvariable=stat, fg="white", bg="black",
                   font=("Calibri 14 bold"), pady=10, padx=2)

bmi_total = Label(root, textvariable=bmi_val, fg="white", bg="black",
                  font=("Calibri 14 bold"), pady=10, padx=2)

bmi.grid(row=6)
status.grid(row=7)
bmi_total.grid(row=6, column=1)
status_msg.grid(row=7, column=1)

calculate = Button(root, text="Calculate", command=calc, fg="black",
                   bg="white", font=("Calibri 12 bold"))

clear = Button(root, text="Reset", command=clear, fg="black",
                   bg="white", font=("Calibri 14 bold"))

calculate.grid(row=8)
clear.grid(row=8, column=3)
root.mainloop()


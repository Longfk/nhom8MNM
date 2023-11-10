import numpy as np
from tkinter import *
import sympy
import tkinter.messagebox
win = Tk()
win.title("Tich Phan")
win.geometry('500x500')
label = Label(win, text="nhap phuong trinh")
label.pack()
entry = Entry(win, width=20)
entry.pack()

label1 = Label(win, text="ket qua")
label1.place(x=10,y=400)

def nutbam1():
    fx = entry.get()
    print(fx)
    x = sympy.Symbol("x")
    daoham = sympy.Derivative(fx, x)
    print(daoham.doit())
    label1.config(text=daoham.doit())


def nutbam2():
    fx = entry.get()
    print(fx)
    x = sympy.Symbol("x")
    tichphan = sympy.integrate(fx, x)
    print(tichphan.doit())
    label1.config(text=tichphan.doit())
def nutbam3():
    fx = entry.get()
    x = sympy.Symbol("x")
    expr = sympy.Poly(fx)
    solutions = sympy.solve(expr)
    label1.config(text=solutions)
def nutbam4():
    fx = entry.get()
    x = sympy.Symbol("x")
    limit = sympy.limit(fx, x, sympy.oo)
    label1.config(text=limit)
bt1 = Button(win, text="đạo hàm", command=nutbam1)
bt1.pack()
bt2 = Button(win, text="tích phân", command=nutbam2)
bt2.pack()
bt3 = Button(win, text="tìm nghiệm", command=nutbam3)
bt3.pack()
bt4 = Button(win, text="giới hạn", command=nutbam4)
bt4.pack()
win.mainloop()
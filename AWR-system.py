import random
import time;
import datetime
import tkinter.messagebox
from tkinter import*

root=Tk()
root.geometry("1350x750+0+0")
root.title("AW Restaurant Management system")
root.configure(background = 'Cadet Blue')

Tops = Frame(root, bg='Cadet Blue', bd=20, pady=5, relief=RIDGE)
Tops.pack(side=TOP)
lblTitle = Label(Tops,font=('arial',50,'bold'),text="AW Restaurant Management system", bd=21,bg='Cadet Blue', fg='Cornsilk', justify=CENTER)
lblTitle.grid(row=0,column=0)

ReceiptCal_f = Frame(root ,bg="Powder Blue", bd=10, relief=RIDGE)
ReceiptCal_f.pack(side=RIGHT)

Buttons_F=Frame(ReceiptCal_f, bg='Powder Blue', bd=3, relief=RIDGE)
Buttons_F.pack(side=BOTTOM)

Cal_F=Frame(ReceiptCal_f,bg='Powder Blue',bd=6, relief=RIDGE)
Cal_F.pack(side=TOP)

Receipt_F=Frame(ReceiptCal_f, bg='Powder Blue', bd=4, relief=RIDGE)
Receipt_F.pack(side=BOTTOM)

MenuFrame = Frame(root, bg='Cadet Blue', bd=10, relief=RIDGE)
MenuFrame.pack(side=LEFT)
Cost_F=Frame(MenuFrame, bg='Cadet Blue', bd=4)
Cost_F.pack(side=BOTTOM)
Drinks_F=Frame(MenuFrame, bg='Cadet Blue', bd=10)
Drinks_F.pack(side=TOP)

Drinks_F=Frame(MenuFrame, bg='Cadet Blue', bd=10, relief=RIDGE)
Drinks_F.pack(side=LEFT)
Cake_F=Frame(MenuFrame, bg='Cadet Blue', bd=10, relief=RIDGE)
Cake_F.pack(side=RIGHT)



root.mainloop()

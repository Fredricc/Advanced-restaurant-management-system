from ast import operator
import random
import time;
import datetime
import tkinter.messagebox
from tkinter import*

root=Tk()
root.geometry("1300x750+0+0")
root.title("AW Restaurant Management system")
root.configure(background = 'Cadet Blue')

Tops = Frame(root, bg='Cadet Blue', bd=20, pady=5, relief=RIDGE)
Tops.pack(side=TOP)
lblTitle = Label(Tops,font=('arial',52,'bold'),text="AW Restaurant Management system", bd=21,bg='Cadet Blue', fg='Cornsilk', justify=CENTER)
lblTitle.grid(row=0,column=0)

ReceiptCal_f = Frame(root ,bg="Powder Blue", bd=10, relief=RIDGE)
ReceiptCal_f.pack(side=RIGHT)

Buttons_F=Frame(ReceiptCal_f, bg='Powder Blue', bd=3, relief=RIDGE)
Buttons_F.pack(side=BOTTOM)

Cal_F=Frame(ReceiptCal_f,bg='Powder Blue',bd=6, relief=RIDGE)
Cal_F.pack(side=TOP)

Receipt_F=Frame(ReceiptCal_f, bg='Powder Blue', bd=3, relief=RIDGE)
Receipt_F.pack(side=BOTTOM)

MenuFrame = Frame(root, bg='Cadet Blue', bd=10, relief=RIDGE)
MenuFrame.pack(side=LEFT)
Cost_F=Frame(MenuFrame, bg='Powder Blue', bd=4)
Cost_F.pack(side=BOTTOM)
Drinks_F=Frame(MenuFrame, bg='Cadet Blue', bd=10)
Drinks_F.pack(side=TOP)

Drinks_F=Frame(MenuFrame, bg='Powder Blue', bd=10, relief=RIDGE)
Drinks_F.pack(side=LEFT)
Cake_F=Frame(MenuFrame, bg='Powder Blue', bd=10, relief=RIDGE)
Cake_F.pack(side=RIGHT)

#========================Variables===================

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
var17=IntVar()
var18=IntVar()


Dateoforder = StringVar()
Receipt_Ref = StringVar()
PaidTax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
CostofDrinks = StringVar()
CostofCakes = StringVar()
ServiceCharge = StringVar()

text_Input = StringVar()
operator=""


E_Latta = StringVar()
E_Espresso = StringVar()
E_Iced_Latta = StringVar()
E_Vale_Coffee = StringVar()
E_Cappuccino = StringVar()
E_African_Coffee = StringVar()
E_American_Coffee = StringVar()
E_Iced_Cappuccino = StringVar()
E_House_Coffee = StringVar()


E_SchoolCake = StringVar() 
E_Sunny_AO_Cake = StringVar()
E_Jonathan_YO_Cake = StringVar()
E_West_African_Cake = StringVar()
E_Nairobi_Chocolate_Cake = StringVar()
E_Strawberry_Cheese_Cake = StringVar()
E_Kilburn_Chocolate_Cake = StringVar()
E_Cariton_Hill_Cake = StringVar()
E_Queen_Park_Cake = StringVar()

E_Latta.set("0")
E_Espresso.set("0")
E_Iced_Latta.set("0")
E_Vale_Coffee.set("0")
E_Cappuccino.set("0")
E_African_Coffee.set("0")
E_American_Coffee.set("0")
E_Iced_Cappuccino.set("0")
E_House_Coffee.set("0")


E_SchoolCake.set("0")
E_Sunny_AO_Cake.set("0")
E_Jonathan_YO_Cake.set("0")
E_West_African_Cake.set("0")
E_Nairobi_Chocolate_Cake.set("0")
E_Strawberry_Cheese_Cake.set("0")
E_Kilburn_Chocolate_Cake.set("0")
E_Cariton_Hill_Cake.set("0")
E_Queen_Park_Cake.set("0")

Dateoforder.set(time.strftime("%d/%m/%Y"))

#========================Drinks===================

Latta =Checkbutton(Drinks_F, text="Latta\t\t\t\t\t", variable=var1, onvalue =1, offvalue=0, font=('arial',10,'bold'), bg='Powder Blue').grid(row=0, sticky=W)
Espresso =Checkbutton(Drinks_F, text="Espresso", variable=var2, onvalue =1, offvalue=0, font=('arial',10,'bold'), bg='Powder Blue').grid(row=1, sticky=W)
Iced_Latta =Checkbutton(Drinks_F, text="Iced Latta", variable=var3, onvalue =1, offvalue=0, font=('arial',10,'bold'), bg='Powder Blue').grid(row=2, sticky=W)
Vale_Coffee =Checkbutton(Drinks_F, text="Vale Coffee", variable=var4, onvalue =1, offvalue=0, font=('arial',10,'bold'), bg='Powder Blue').grid(row=3, sticky=W)
Cappuccino =Checkbutton(Drinks_F, text="Cappuccino", variable=var5, onvalue =1, offvalue=0, font=('arial',10,'bold'), bg='Powder Blue').grid(row=4, sticky=W)
African_Coffee =Checkbutton(Drinks_F, text="African_Coffee", variable=var6, onvalue =1, offvalue=0, font=('arial',10,'bold'), bg='Powder Blue').grid(row=5, sticky=W)
American_Coffee =Checkbutton(Drinks_F, text="American_Coffee", variable=var7, onvalue =1, offvalue=0, font=('arial',10,'bold'), bg='Powder Blue').grid(row=6, sticky=W)
Iced_Cappuccino =Checkbutton(Drinks_F, text="Iced_Cappuccino", variable=var8, onvalue =1, offvalue=0, font=('arial',10,'bold'), bg='Powder Blue').grid(row=7, sticky=W)
House_Coffee =Checkbutton(Drinks_F, text="House_Coffee", variable=var9, onvalue =1, offvalue=0, font=('arial',10,'bold'), bg='Powder Blue').grid(row=8, sticky=W)

#========================Entry Box for Drinks===================

txtLatta = Entry(Drinks_F,font=('arial',12,'bold'),bd=8, width=6 , justify=LEFT, state=DISABLED)
txtLatta.grid(row=0,column=1)
txtEspresso = Entry(Drinks_F,font=('arial',12,'bold'),bd=8, width=6 , justify=LEFT, state=DISABLED)
txtEspresso.grid(row=1,column=1)
txtIced_Latta = Entry(Drinks_F,font=('arial',12,'bold'),bd=8, width=6 , justify=LEFT, state=DISABLED)
txtIced_Latta.grid(row=2,column=1)
txtVale_Coffee = Entry(Drinks_F,font=('arial',12,'bold'),bd=8, width=6 , justify=LEFT, state=DISABLED)
txtVale_Coffee.grid(row=3,column=1)
txtCappuccino = Entry(Drinks_F,font=('arial',12,'bold'),bd=8, width=6 , justify=LEFT, state=DISABLED)
txtCappuccino.grid(row=4,column=1)
txtAfrican_Coffee = Entry(Drinks_F,font=('arial',12,'bold'),bd=8, width=6 , justify=LEFT, state=DISABLED)
txtAfrican_Coffee.grid(row=5,column=1)
txtAmerican_Coffee = Entry(Drinks_F,font=('arial',12,'bold'),bd=8, width=6 , justify=LEFT, state=DISABLED)
txtAmerican_Coffee.grid(row=6,column=1)
txtIced_Cappuccino = Entry(Drinks_F,font=('arial',12,'bold'),bd=8, width=6 , justify=LEFT, state=DISABLED)
txtIced_Cappuccino.grid(row=7,column=1)
txtHouse_Coffee = Entry(Drinks_F,font=('arial',12,'bold'),bd=8, width=6 , justify=LEFT, state=DISABLED)
txtHouse_Coffee.grid(row=8,column=1)

#========================Cakes===================

SchoolCake =Checkbutton(Cake_F, text="SchoolCake\t\t\t\t", variable=var10, onvalue =1, offvalue=0, font=('arial',10,'bold'), bg='Powder Blue').grid(row=0, sticky=W)
Sunny_AO_Cake =Checkbutton(Cake_F, text="Sunny_AO_Cake", variable=var11, onvalue =1, offvalue=0, font=('arial',10,'bold'), bg='Powder Blue').grid(row=1, sticky=W)
Jonathan_YO_Cake =Checkbutton(Cake_F, text="Jonathan O Cake", variable=var12, onvalue =1, offvalue=0, font=('arial',10,'bold'), bg='Powder Blue').grid(row=2, sticky=W)
West_African_Cake =Checkbutton(Cake_F, text="West African Cake", variable=var13, onvalue =1, offvalue=0, font=('arial',10,'bold'), bg='Powder Blue').grid(row=3, sticky=W)
Nairobi_Chocolate_Cake =Checkbutton(Cake_F, text="Nairobi Chocolate Cake", variable=var14, onvalue =1, offvalue=0, font=('arial',10,'bold'), bg='Powder Blue').grid(row=4, sticky=W)
Strawberry_Cheese_Cake =Checkbutton(Cake_F, text="Strawberry Cheesecake", variable=var15, onvalue =1, offvalue=0, font=('arial',10,'bold'), bg='Powder Blue').grid(row=5, sticky=W)
Kilburn_Chocolate_Cake =Checkbutton(Cake_F, text="Kilburn Chocolate Cake", variable=var16, onvalue =1, offvalue=0, font=('arial',10,'bold'), bg='Powder Blue').grid(row=6, sticky=W)
Cariton_Hill_Cake =Checkbutton(Cake_F, text="Cariton Hill Cake", variable=var17, onvalue =1, offvalue=0, font=('arial',10,'bold'), bg='Powder Blue').grid(row=7, sticky=W)
Queen_Park_Cake =Checkbutton(Cake_F, text="Queen Park Cake", variable=var18, onvalue =1, offvalue=0, font=('arial',10,'bold'), bg='Powder Blue').grid(row=8, sticky=W)

#========================Entry Box for Cakes===================
txtSchoolCake = Entry(Cake_F,font=('arial',12,'bold'),bd=8, width=6 , justify=LEFT, state=DISABLED)
txtSchoolCake.grid(row=0,column=1)
txtSunny_AO_Cake = Entry(Cake_F,font=('arial',12,'bold'),bd=8, width=6 , justify=LEFT, state=DISABLED)
txtSunny_AO_Cake.grid(row=1,column=1)
txtJonathan_YO_Cake = Entry(Cake_F,font=('arial',12,'bold'),bd=8, width=6 , justify=LEFT, state=DISABLED)
txtJonathan_YO_Cake.grid(row=2,column=1)
txtWest_African_Cake = Entry(Cake_F,font=('arial',12,'bold'),bd=8, width=6 , justify=LEFT, state=DISABLED)
txtWest_African_Cake.grid(row=3,column=1)
txtNairobi_Chocolate_Cake = Entry(Cake_F,font=('arial',12,'bold'),bd=8, width=6 , justify=LEFT, state=DISABLED)
txtNairobi_Chocolate_Cake.grid(row=4,column=1)
txtStrawberry_Cheese_Cake = Entry(Cake_F,font=('arial',12,'bold'),bd=8, width=6 , justify=LEFT, state=DISABLED)
txtStrawberry_Cheese_Cake.grid(row=5,column=1)
txtKilburn_Chocolate_Cake = Entry(Cake_F,font=('arial',12,'bold'),bd=8, width=6 , justify=LEFT, state=DISABLED)
txtKilburn_Chocolate_Cake.grid(row=6,column=1)
txtCariton_Hill_Cake = Entry(Cake_F,font=('arial',12,'bold'),bd=8, width=6 , justify=LEFT, state=DISABLED)
txtCariton_Hill_Cake.grid(row=7,column=1)
txtQueen_Park_Cake = Entry(Cake_F,font=('arial',12,'bold'),bd=8, width=6 , justify=LEFT, state=DISABLED)
txtQueen_Park_Cake.grid(row=8,column=1)

#========================Total Cost===============

lblCostofDrinks = Label(Cost_F,font=('arial',12,'bold'),text="Cost of Drinks\t ",bg='Powder Blue', fg='Black')
lblCostofDrinks.grid(row=0,column=0, sticky=W)
txtCostofDrinks = Entry(Cost_F,font=('arial',12,'bold'), bg='white', bd=7, insertwidth=2, justify=RIGHT)
txtCostofDrinks.grid(row=0, column=1)

lblCostofCakes = Label(Cost_F,font=('arial',12,'bold'),text="Cost of Cakes\t ",bg='Powder Blue', fg='Black')
lblCostofCakes.grid(row=1,column=0, sticky=W)
txtCostofCakes = Entry(Cost_F,font=('arial',12,'bold'), bg='white', bd=7, insertwidth=2, justify=RIGHT)
txtCostofCakes.grid(row=1, column=1)

lblServiceCharge = Label(Cost_F,font=('arial',12,'bold'),text="Service Charge\t ",bg='Powder Blue', fg='Black')
lblServiceCharge.grid(row=2,column=0, sticky=W)
txtServiceCharge = Entry(Cost_F,font=('arial',12,'bold'), bg='white', bd=7, insertwidth=2, justify=RIGHT)
txtServiceCharge.grid(row=2, column=1)

#========================payment information===============

lblPaidTax = Label(Cost_F,font=('arial',12,'bold'),text="\tPaid Tax\t ",bd=7, bg='Powder Blue', fg='Black')
lblPaidTax.grid(row=0,column=2, sticky=W)
txtPaidTax = Entry(Cost_F,font=('arial',12,'bold'), bg='white', bd=7, insertwidth=2, justify=RIGHT)
txtPaidTax.grid(row=0, column=3)

lblSubTotal = Label(Cost_F,font=('arial',12,'bold'),text="\tSub Total\t ",bd=7,bg='Powder Blue', fg='Black')
lblSubTotal.grid(row=1,column=2, sticky=W)
txtSubTotal = Entry(Cost_F,font=('arial',12,'bold'), bg='white', bd=7, insertwidth=2, justify=RIGHT)
txtSubTotal.grid(row=1, column=3)

lblTotalCost = Label(Cost_F,font=('arial',12,'bold'),text="\t Total Cost ",bd=7,bg='Powder Blue', fg='Black')
lblTotalCost.grid(row=2,column=2, sticky=W)
txtTotalCost = Entry(Cost_F,font=('arial',12,'bold'), bg='white', bd=7, insertwidth=2, justify=RIGHT)
txtTotalCost.grid(row=2, column=3)


#========================Receipt===============
txtReceipt = Text(Receipt_F, width=46, height=12, bg='white', bd=4, font=('arial', 12, 'bold'))
txtReceipt.grid(row=0, column=0)

#========================Buttons==============
btnTotal = Button(Buttons_F,padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'), width=4, text='Total', bg='powder blue').grid(row=0, column=0)
btnReceipt = Button(Buttons_F,padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'), width=4, text='Receipt', bg='powder blue').grid(row=0, column=1)
btnReset = Button(Buttons_F,padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'), width=4, text='Reset', bg='powder blue').grid(row=0, column=2)
btnExit = Button(Buttons_F,padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'), width=4, text='Exit', bg='powder blue').grid(row=0, column=3)

#========================Calculator Display==============

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)
    
def btnClear():
    global operator
    operator= ""
    text_Input.set("")
    
def btnEquals():
    global operator
    sump = str(eval(operator))
    text_Input.set(sump)
    operator =""

txtDisplay = Entry(Cal_F, width=45, bg='white', bd=4, font=('arial', 12, 'bold'), justify=RIGHT, textvariable=text_Input)
txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
txtDisplay.insert(0, "0")

#========================Calculator Buttons==============
btn7 = Button(Cal_F,padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'), width=4, text='7', bg='powder blue', command=lambda:btnClick(7)).grid(row=2, column=0)

btn8 = Button(Cal_F,padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'), width=4, text='8', bg='powder blue', command=lambda:btnClick(8)).grid(row=2, column=1)

btn9 = Button(Cal_F,padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'), width=4, text='9', bg='powder blue', command=lambda:btnClick(9)).grid(row=2, column=2)

btnAdd = Button(Cal_F,padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'), width=4, text='+', bg='powder blue', command=lambda:btnClick("+")).grid(row=2, column=3)

#========================Calculator Buttons==============
btn4 = Button(Cal_F,padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'), width=4, text='4', bg='powder blue', command=lambda:btnClick(4)).grid(row=3, column=0)
btn5 = Button(Cal_F,padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'), width=4, text='5', bg='powder blue', command=lambda:btnClick(5)).grid(row=3, column=1)
btn6 = Button(Cal_F,padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'), width=4, text='6', bg='powder blue', command=lambda:btnClick(6)).grid(row=3, column=2)
btnSubt = Button(Cal_F,padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'), width=4, text='-', bg='powder blue', command=lambda:btnClick("-")).grid(row=3, column=3)

#========================Calculator Buttons==============
btn1 = Button(Cal_F,padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'), width=4, text='1', bg='powder blue', command=lambda:btnClick(1)).grid(row=4, column=0)
btn2 = Button(Cal_F,padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'), width=4, text='2', bg='powder blue', command=lambda:btnClick(2)).grid(row=4, column=1)
btn3 = Button(Cal_F,padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'), width=4, text='3', bg='powder blue', command=lambda:btnClick(3)).grid(row=4, column=2)
btnMulti = Button(Cal_F,padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'), width=4, text='x', bg='powder blue', command=lambda:btnClick("*")).grid(row=4, column=3)

#========================Calculator Buttons==============
btn0 = Button(Cal_F,padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'), width=4, text='0', bg='powder blue', command=lambda:btnClick(0)).grid(row=5, column=0)
btnClear = Button(Cal_F,padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'), width=4, text='C', bg='powder blue', command=btnClear).grid(row=5, column=1)
btnEquals = Button(Cal_F,padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'), width=4, text='=', bg='powder blue', command=btnEquals).grid(row=5, column=2)
btnDiv = Button(Cal_F,padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'), width=4, text='/', bg='powder blue', command=lambda:btnClick("/")).grid(row=5, column=3)


root.mainloop()

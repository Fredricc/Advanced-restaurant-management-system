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
E_Iced_Latte = StringVar()
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
E_Iced_Latte.set("0")
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

#=========================Exit Function================


def iExit():
    iExit = tkinter.messagebox.askyesno("Exit Restaurant System","Confirm if you want to exit")
    if iExit > 0:
        root.destroy()
        return

def Reset():
    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    CostofDrinks.set("")
    CostofCakes.set("")
    ServiceCharge.set("")
    txtReceipt.delete("1.0".END)

    
    E_Latta.set("0")
    E_Espresso.set("0")
    E_Iced_Latte.set("0")
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
    
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)

    txtLatta.configure(state = DISABLED)
    txtEspresso.configure(state = DISABLED)
    txtIced_Latte.configure(state = DISABLED)
    txtVale_Coffee.configure(state = DISABLED)
    txtCappuccino.configure(state = DISABLED)
    txtAfrican_Coffee.configure(state = DISABLED)
    txtAmerican_Coffee.configure(state = DISABLED)
    txtIced_Cappuccino.configure(state = DISABLED)
    txtHouse_Coffee.configure(state = DISABLED)


    txtSchoolCake.configure(state = DISABLED)
    txtSunny_AO_Cake.configure(state = DISABLED)
    txtJonathan_YO_Cake.configure(state = DISABLED)
    txtWest_African_Cake.configure(state = DISABLED)
    txtNairobi_Chocolate_Cake.configure(state = DISABLED)
    txtStrawberry_Cheese_Cake.configure(state = DISABLED)
    txtKilburn_Chocolate_Cake.configure(state = DISABLED)
    txtCariton_Hill_Cake.configure(state = DISABLED)
    txtQueen_Park_Cake.configure(state = DISABLED)
    
def CostofItem():
    Item1=float (E_Latta.get())
    Item2=float (E_Espresso.get())
    Item3=float (E_Iced_Latte.get())
    Item4=float (E_Vale_Coffee.get())
    Item5=float (E_Cappuccino.get())
    Item6=float (E_African_Coffee.get())
    Item7=float (E_American_Coffee.get())
    Item8=float (E_Iced_Cappuccino.get())
    Item9=float (E_House_Coffee.get())


    Item10=float (E_SchoolCake.get())
    Item11=float (E_Sunny_AO_Cake.get())
    Item12=float (E_Jonathan_YO_Cake.get())
    Item13=float (E_West_African_Cake.get())
    Item14=float (E_Nairobi_Chocolate_Cake.get())
    Item15=float (E_Strawberry_Cheese_Cake.get())
    Item16=float (E_Kilburn_Chocolate_Cake.get())
    Item17=float (E_Cariton_Hill_Cake.get())
    Item18=float (E_Queen_Park_Cake.get())
    
    PriceofDrinks =(Item1* 1.2) + (Item2 * 1.99) + (Item3 * 2.05) \
        + (Item4* 1.89) + (Item5 * 1.99) + (Item6 * 2.99) + (Item7 * 2.39) + (Item8 * 1.2) + (Item9 * 1.34)
        
    PriceofCakes = (Item10* 1.35) + (Item11* 2.2) + (Item12 * 1.99) \
        + (Item13 * 1.49) + (Item14 * 1.8) + (Item15 * 1.67) + (Item16 * 1.6) + (Item17* 1.99) + (Item18 * 1.28)
        
    DrinksPrice = "$", str('%.2f'%( PriceofDrinks))
    CakesPrice="$", str('%.2f'%(PriceofCakes))
    CostofCakes.set(CakesPrice)
    CostofDrinks.set(DrinksPrice)
    SC="$", str('%.2f'%(1.59))
    ServiceCharge.set(SC)
    
    SubTotalofITEMS = "$", str('%.2f'%(PriceofDrinks + PriceofCakes + 1.59))
    SubTotal.set(SubTotalofITEMS)
    
    Tax="$", str('%.2f'%((PriceofDrinks + PriceofCakes + 1.59)*0.15))
    PaidTax.set(Tax)
    TT=((PriceofDrinks + PriceofCakes + 1.59)*0.15)
    TC="$",str('%.2f'%(PriceofDrinks + PriceofCakes + 1.59 + TT))
    TotalCost.set(TC)    
    
        
def chkLatta():
    if (var1.get() == 1):
        txtLatta.configure(state = NORMAL)
        txtLatta.focus()
        txtLatta.delete('0', END)
        E_Latta.set("")
    elif(var1.get() == 0):
        txtLatta.configure(state = NORMAL)
        E_Latta.set("0")    
    
    
def chkEspresso():
    if (var1.get() == 1):
        txtEspresso.configure(state = NORMAL)
        txtEspresso.focus()
        txtEspresso.delete('0', END)
        E_Espresso.set("")
    elif(var1.get() == 0):
        txtEspresso.configure(state = NORMAL)
        E_Espresso.set("0")

def chkIced_Latte():
    if (var1.get() == 1):
        txtIced_Latte.configure(state = NORMAL)
        txtIced_Latte.focus()
        txtIced_Latte.delete('0', END)
        E_Iced_Latte.set("")
    elif(var1.get() == 0):
        txtIced_Latte.configure(state = NORMAL)
        E_Iced_Latte.set("0")
        
def chkVale_Coffee():
    if (var1.get() == 1):
        txtVale_Coffee.configure(state = NORMAL)
        txtVale_Coffee.focus()
        txtVale_Coffee.delete('0', END)
        E_Vale_Coffee.set("")
    elif(var1.get() == 0):
        txtVale_Coffee.configure(state = NORMAL)
        E_Vale_Coffee.set("0")
        
def chkCappuccino():
    if (var1.get() == 1):
        txtCappuccino.configure(state = NORMAL)
        txtCappuccino.focus()
        txtCappuccino.delete('0', END)
        E_Cappuccino.set("")
    elif(var1.get() == 0):
        txtCappuccino.configure(state = NORMAL)
        E_Cappuccino.set("0")
        
def chkAfrican_Coffee():
    if (var1.get() == 1):
        txtAfrican_Coffee.configure(state = NORMAL)
        txtAfrican_Coffee.focus()
        txtAfrican_Coffee.delete('0', END)
        E_African_Coffee.set("")
    elif(var1.get() == 0):
        txtAfrican_Coffee.configure(state = NORMAL)
        E_African_Coffee.set("0")
        
def chkAmerican_Coffee():
    if (var1.get() == 1):
        txtAmerican_Coffee.configure(state = NORMAL)
        txtAmerican_Coffee.focus()
        txtAmerican_Coffee.delete('0', END)
        E_American_Coffee.set("")
    elif(var1.get() == 0):
        txtAmerican_Coffee.configure(state = NORMAL)
        E_American_Coffee.set("0")
        
def chkIced_Cappuccino():
    if (var1.get() == 1):
        txtIced_Cappuccino.configure(state = NORMAL)
        txtIced_Cappuccino.focus()
        txtIced_Cappuccino.delete('0', END)
        E_Iced_Cappuccino.set("")
    elif(var1.get() == 0):
        txtIced_Cappuccino.configure(state = NORMAL)
        E_Iced_Cappuccino.set("0")
        
def chkHouse_Coffee():
    if (var1.get() == 1):
        txtHouse_Coffee.configure(state = NORMAL)
        txtHouse_Coffee.focus()
        txtHouse_Coffee.delete('0', END)
        E_House_Coffee.set("")
    elif(var1.get() == 0):
        txtHouse_Coffee.configure(state = NORMAL)
        E_House_Coffee.set("0")
        
def chkSchoolCake():
    if (var1.get() == 1):
        txtSchoolCake.configure(state = NORMAL)
        txtSchoolCake.focus()
        txtSchoolCake.delete('0', END)
        E_SchoolCake.set("")
    elif(var1.get() == 0):
        txtSchoolCake.configure(state = NORMAL)
        E_SchoolCake.set("0")
        
def chkSunny_AO_Cake():
    if (var1.get() == 1):
        txtSunny_AO_Cake.configure(state = NORMAL)
        txtSunny_AO_Cake.focus()
        txtSunny_AO_Cake.delete('0', END)
        E_Sunny_AO_Cake.set("")
    elif(var1.get() == 0):
        txtSunny_AO_Cake.configure(state = NORMAL)
        E_Sunny_AO_Cake.set("0")
        
def chkJonathan_YO_Cake():
    if (var1.get() == 1):
        txtJonathan_YO_Cake.configure(state = NORMAL)
        txtJonathan_YO_Cake.focus()
        txtJonathan_YO_Cake.delete('0', END)
        E_Jonathan_YO_Cake.set("")
    elif(var1.get() == 0):
        txtJonathan_YO_Cake.configure(state = NORMAL)
        E_Jonathan_YO_Cake.set("0")
        
def chkWest_African_Cake():
    if (var1.get() == 1):
        txtWest_African_Cake.configure(state = NORMAL)
        txtWest_African_Cake.focus()
        txtWest_African_Cake.delete('0', END)
        E_West_African_Cake.set("")
    elif(var1.get() == 0):
        txtWest_African_Cake.configure(state = NORMAL)
        E_West_African_Cake.set("0")
        
def chkNairobi_Chocolate_Cake():
    if (var1.get() == 1):
        txtNairobi_Chocolate_Cake.configure(state = NORMAL)
        txtNairobi_Chocolate_Cake.focus()
        txtNairobi_Chocolate_Cake.delete('0', END)
        E_Nairobi_Chocolate_Cake.set("")
    elif(var1.get() == 0):
        txtNairobi_Chocolate_Cake.configure(state = NORMAL)
        E_Nairobi_Chocolate_Cake.set("0")
        
def chkStrawberry_Cheese_Cake():
    if (var1.get() == 1):
        txtStrawberry_Cheese_Cake.configure(state = NORMAL)
        txtStrawberry_Cheese_Cake.focus()
        txtStrawberry_Cheese_Cake.delete('0', END)
        E_Strawberry_Cheese_Cake.set("")
    elif(var1.get() == 0):
        txtStrawberry_Cheese_Cake.configure(state = NORMAL)
        E_Strawberry_Cheese_Cake.set("0")
        
def chkKilburn_Chocolate_Cake():
    if (var1.get() == 1):
        txtKilburn_Chocolate_Cake.configure(state = NORMAL)
        txtKilburn_Chocolate_Cake.focus()
        txtKilburn_Chocolate_Cake.delete('0', END)
        E_Kilburn_Chocolate_Cake.set("")
    elif(var1.get() == 0):
        txtKilburn_Chocolate_Cake.configure(state = NORMAL)
        E_Kilburn_Chocolate_Cake.set("0")
        
def chkCariton_Hill_Cake():
    if (var1.get() == 1):
        txtCariton_Hill_Cake.configure(state = NORMAL)
        txtCariton_Hill_Cake.focus()
        txtCariton_Hill_Cake.delete('0', END)
        E_Cariton_Hill_Cake.set("")
    elif(var1.get() == 0):
        txtCariton_Hill_Cake.configure(state = NORMAL)
        E_Cariton_Hill_Cake.set("0")
        
def chkQueen_Park_Cake():
    if (var1.get() == 1):
        txtQueen_Park_Cake.configure(state = NORMAL)
        txtQueen_Park_Cake.focus()
        txtQueen_Park_Cake.delete('0', END)
        E_Queen_Park_Cake.set("")
    elif(var1.get() == 0):
        txtQueen_Park_Cake.configure(state = NORMAL)
        E_Queen_Park_Cake.set("0")
        
        
#========================Drinks===================

Latta =Checkbutton(Drinks_F, text="Latta\t\t\t\t\t", variable=var1, onvalue =1, offvalue=0, font=('arial',10,'bold'), bg='Powder Blue', command = chkLatta ).grid(row=0, sticky=W)

Espresso =Checkbutton(Drinks_F, text="Espresso", variable=var2, onvalue =1, offvalue=0, font=('arial',10,'bold'), bg='Powder Blue', command = chkEspresso ).grid(row=1, sticky=W)

Iced_Latte =Checkbutton(Drinks_F, text="Iced Latta", variable=var3, onvalue =1, offvalue=0, font=('arial',10,'bold'), bg='Powder Blue', command = chkIced_Latte ).grid(row=2, sticky=W)

Vale_Coffee =Checkbutton(Drinks_F, text="Vale Coffee", variable=var4, onvalue =1, offvalue=0, font=('arial',10,'bold'), bg='Powder Blue', command = chkVale_Coffee ).grid(row=3, sticky=W)

Cappuccino =Checkbutton(Drinks_F, text="Cappuccino", variable=var5, onvalue =1, offvalue=0, font=('arial',10,'bold'), bg='Powder Blue', command = chkCappuccino ).grid(row=4, sticky=W)

African_Coffee =Checkbutton(Drinks_F, text="African_Coffee", variable=var6, onvalue =1, offvalue=0, font=('arial',10,'bold'), bg='Powder Blue', command = chkAfrican_Coffee ).grid(row=5, sticky=W)

American_Coffee =Checkbutton(Drinks_F, text="American_Coffee", variable=var7, onvalue =1, offvalue=0, font=('arial',10,'bold'), bg='Powder Blue', command = chkAmerican_Coffee ).grid(row=6, sticky=W)

Iced_Cappuccino =Checkbutton(Drinks_F, text="Iced_Cappuccino", variable=var8, onvalue =1, offvalue=0, font=('arial',10,'bold'), bg='Powder Blue', command = chkIced_Cappuccino ).grid(row=7, sticky=W)

House_Coffee =Checkbutton(Drinks_F, text="House_Coffee", variable=var9, onvalue =1, offvalue=0, font=('arial',10,'bold'), bg='Powder Blue', command = chkHouse_Coffee ).grid(row=8, sticky=W)

#========================Entry Box for Drinks===================

txtLatta = Entry(Drinks_F,font=('arial',12,'bold'),bd=8, width=6 , justify=LEFT, state=DISABLED, textvariable = E_Latta)
txtLatta.grid(row=0,column=1)

txtEspresso = Entry(Drinks_F,font=('arial',12,'bold'),bd=8, width=6 , justify=LEFT, state=DISABLED, textvariable = E_Espresso)
txtEspresso.grid(row=1,column=1)

txtIced_Latte = Entry(Drinks_F,font=('arial',12,'bold'),bd=8, width=6 , justify=LEFT, state=DISABLED, textvariable = E_Iced_Latte)

txtIced_Latte.grid(row=2,column=1)
txtVale_Coffee = Entry(Drinks_F,font=('arial',12,'bold'),bd=8, width=6 , justify=LEFT, state=DISABLED, textvariable = E_Vale_Coffee)

txtVale_Coffee.grid(row=3,column=1)
txtCappuccino = Entry(Drinks_F,font=('arial',12,'bold'),bd=8, width=6 , justify=LEFT, state=DISABLED, textvariable = E_Cappuccino)

txtCappuccino.grid(row=4,column=1)
txtAfrican_Coffee = Entry(Drinks_F,font=('arial',12,'bold'),bd=8, width=6 , justify=LEFT, state=DISABLED, textvariable = E_African_Coffee)

txtAfrican_Coffee.grid(row=5,column=1)
txtAmerican_Coffee = Entry(Drinks_F,font=('arial',12,'bold'),bd=8, width=6 , justify=LEFT, state=DISABLED, textvariable = E_American_Coffee)
txtAmerican_Coffee.grid(row=6,column=1)

txtIced_Cappuccino = Entry(Drinks_F,font=('arial',12,'bold'),bd=8, width=6 , justify=LEFT, state=DISABLED, textvariable = E_Iced_Cappuccino)
txtIced_Cappuccino.grid(row=7,column=1)

txtHouse_Coffee = Entry(Drinks_F,font=('arial',12,'bold'),bd=8, width=6 , justify=LEFT, state=DISABLED, textvariable = E_House_Coffee)
txtHouse_Coffee.grid(row=8,column=1)

#========================Cakes===================

SchoolCake =Checkbutton(Cake_F, text="SchoolCake\t\t\t\t", variable=var10, onvalue =1, offvalue=0, font=('arial',10,'bold'), bg='Powder Blue', command = chkSchoolCake ).grid(row=0, sticky=W)

Sunny_AO_Cake =Checkbutton(Cake_F, text="Sunny_AO_Cake", variable=var11, onvalue =1, offvalue=0, font=('arial',10,'bold'), bg='Powder Blue', command = chkSunny_AO_Cake ).grid(row=1, sticky=W)

Jonathan_YO_Cake =Checkbutton(Cake_F, text="Jonathan O Cake", variable=var12, onvalue =1, offvalue=0, font=('arial',10,'bold'), bg='Powder Blue', command = chkJonathan_YO_Cake ).grid(row=2, sticky=W)

West_African_Cake =Checkbutton(Cake_F, text="West African Cake", variable=var13, onvalue =1, offvalue=0, font=('arial',10,'bold'), bg='Powder Blue', command = chkWest_African_Cake ).grid(row=3, sticky=W)

Nairobi_Chocolate_Cake =Checkbutton(Cake_F, text="Nairobi Chocolate Cake", variable=var14, onvalue =1, offvalue=0, font=('arial',10,'bold'), bg='Powder Blue', command = chkNairobi_Chocolate_Cake ).grid(row=4, sticky=W)

Strawberry_Cheese_Cake =Checkbutton(Cake_F, text="Strawberry Cheesecake", variable=var15, onvalue =1, offvalue=0, font=('arial',10,'bold'), bg='Powder Blue', command = chkStrawberry_Cheese_Cake ).grid(row=5, sticky=W)

Kilburn_Chocolate_Cake =Checkbutton(Cake_F, text="Kilburn Chocolate Cake", variable=var16, onvalue =1, offvalue=0, font=('arial',10,'bold'), bg='Powder Blue', command = chkKilburn_Chocolate_Cake ).grid(row=6, sticky=W)

Cariton_Hill_Cake =Checkbutton(Cake_F, text="Cariton Hill Cake", variable=var17, onvalue =1, offvalue=0, font=('arial',10,'bold'), bg='Powder Blue', command = chkCariton_Hill_Cake ).grid(row=7, sticky=W)

Queen_Park_Cake =Checkbutton(Cake_F, text="Queen Park Cake", variable=var18, onvalue =1, offvalue=0, font=('arial',10,'bold'), bg='Powder Blue', command = chkQueen_Park_Cake ).grid(row=8, sticky=W)

#========================Entry Box for Cakes===================
txtSchoolCake = Entry(Cake_F,font=('arial',12,'bold'),bd=8, width=6 , justify=LEFT, state=DISABLED, textvariable = E_SchoolCake)
txtSchoolCake.grid(row=0,column=1)

txtSunny_AO_Cake = Entry(Cake_F,font=('arial',12,'bold'),bd=8, width=6 , justify=LEFT, state=DISABLED, textvariable = E_Sunny_AO_Cake)
txtSunny_AO_Cake.grid(row=1,column=1)

txtJonathan_YO_Cake = Entry(Cake_F,font=('arial',12,'bold'),bd=8, width=6 , justify=LEFT, state=DISABLED, textvariable = E_Jonathan_YO_Cake)
txtJonathan_YO_Cake.grid(row=2,column=1)

txtWest_African_Cake = Entry(Cake_F,font=('arial',12,'bold'),bd=8, width=6 , justify=LEFT, state=DISABLED, textvariable = E_West_African_Cake)
txtWest_African_Cake.grid(row=3,column=1)

txtNairobi_Chocolate_Cake = Entry(Cake_F,font=('arial',12,'bold'),bd=8, width=6 , justify=LEFT, state=DISABLED, textvariable = E_Nairobi_Chocolate_Cake)
txtNairobi_Chocolate_Cake.grid(row=4,column=1)

txtStrawberry_Cheese_Cake = Entry(Cake_F,font=('arial',12,'bold'),bd=8, width=6 , justify=LEFT, state=DISABLED, textvariable = E_Strawberry_Cheese_Cake)
txtStrawberry_Cheese_Cake.grid(row=5,column=1)

txtKilburn_Chocolate_Cake = Entry(Cake_F,font=('arial',12,'bold'),bd=8, width=6 , justify=LEFT, state=DISABLED, textvariable = E_Kilburn_Chocolate_Cake)
txtKilburn_Chocolate_Cake.grid(row=6,column=1)

txtCariton_Hill_Cake = Entry(Cake_F,font=('arial',12,'bold'),bd=8, width=6 , justify=LEFT, state=DISABLED, textvariable = E_Cariton_Hill_Cake)
txtCariton_Hill_Cake.grid(row=7,column=1)

txtQueen_Park_Cake = Entry(Cake_F,font=('arial',12,'bold'),bd=8, width=6 , justify=LEFT, state=DISABLED, textvariable = E_Queen_Park_Cake)
txtQueen_Park_Cake.grid(row=8,column=1)

#========================Total Cost===============

lblCostofDrinks = Label(Cost_F,font=('arial',12,'bold'),text="Cost of Drinks\t ",bg='Powder Blue', fg='Black')
lblCostofDrinks.grid(row=0,column=0, sticky=W)
txtCostofDrinks = Entry(Cost_F,font=('arial',12,'bold'), textvariable= CostofDrinks , bg='white', bd=7, insertwidth=2, justify=RIGHT)
txtCostofDrinks.grid(row=0, column=1)

lblCostofCakes = Label(Cost_F,font=('arial',12,'bold'),text="Cost of Cakes\t ",bg='Powder Blue', fg='Black')
lblCostofCakes.grid(row=1,column=0, sticky=W)
txtCostofCakes = Entry(Cost_F,font=('arial',12,'bold'), textvariable= CostofCakes , bg='white', bd=7, insertwidth=2, justify=RIGHT)
txtCostofCakes.grid(row=1, column=1)

lblServiceCharge = Label(Cost_F,font=('arial',12,'bold'),text="Service Charge\t ",bg='Powder Blue', fg='Black')
lblServiceCharge.grid(row=2,column=0, sticky=W)
txtServiceCharge = Entry(Cost_F,font=('arial',12,'bold'), textvariable= ServiceCharge , bg='white', bd=7, insertwidth=2, justify=RIGHT)
txtServiceCharge.grid(row=2, column=1)

#========================payment information===============

lblPaidTax = Label(Cost_F,font=('arial',12,'bold'),text="\tPaid Tax\t ",bd=7, bg='Powder Blue', fg='Black')
lblPaidTax.grid(row=0,column=2, sticky=W)
txtPaidTax = Entry(Cost_F,font=('arial',12,'bold'), textvariable= PaidTax , bg='white', bd=7, insertwidth=2, justify=RIGHT)
txtPaidTax.grid(row=0, column=3)

lblSubTotal = Label(Cost_F,font=('arial',12,'bold'),text="\tSub Total\t ",bd=7,bg='Powder Blue', fg='Black')
lblSubTotal.grid(row=1,column=2, sticky=W)
txtSubTotal = Entry(Cost_F,font=('arial',12,'bold'), textvariable= SubTotal , bg='white', bd=7, insertwidth=2, justify=RIGHT)
txtSubTotal.grid(row=1, column=3)

lblTotalCost = Label(Cost_F,font=('arial',12,'bold'),text="\t Total Cost ",bd=7,bg='Powder Blue', fg='Black')
lblTotalCost.grid(row=2,column=2, sticky=W)
txtTotalCost = Entry(Cost_F,font=('arial',12,'bold'), textvariable= TotalCost , bg='white', bd=7, insertwidth=2, justify=RIGHT)
txtTotalCost.grid(row=2, column=3)


#========================Receipt===============
txtReceipt = Text(Receipt_F, width=46, height=12, bg='white', bd=4, font=('arial', 12, 'bold'))
txtReceipt.grid(row=0, column=0)

#========================Buttons==============
btnTotal = Button(Buttons_F,padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'), width=4, text='Total', bg='powder blue', command= CostofItem ).grid(row=0, column=0)

btnReceipt = Button(Buttons_F,padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'), width=4, text='Receipt', bg='powder blue').grid(row=0, column=1)

btnReset = Button(Buttons_F,padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'), width=4, text='Reset', bg='powder blue', command= Reset).grid(row=0, column=2)

btnExit = Button(Buttons_F,padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'), width=4, text='Exit', bg='powder blue', command= iExit).grid(row=0, column=3)

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

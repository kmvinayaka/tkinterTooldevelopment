from tkinter import*
import random
import time

root = Tk()
root.geometry("890x580+0+0")
root.title("SIMPLE SCHOOL FEE BILLING SYSTEM")

Tops = Frame(root,bg="white",width = 1600,height=50,relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root,width = 900,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root ,width = 400,height=700,relief=SUNKEN)
f2.pack(side=RIGHT)
#------------------TIME--------------
localtime=time.asctime(time.localtime(time.time()))
#-----------------INFO TOP------------
lblinfo = Label(Tops, font=( 'aria' ,30, 'bold' ),text="SIMPLE SCHOOL FEE BILLING SYSTEM",fg="Black",bd=10,anchor='w')
lblinfo.grid(row=0,column=0)
lblinfo = Label(Tops, font=( 'aria' ,20, ),text=localtime,fg="steel blue",anchor=W)
lblinfo.grid(row=1,column=0)


def Ref():
    x=random.randint(12980, 50876)
    randomRef = str(x)
    rand.set(randomRef)

    cof =float(sports.get())
    coll= float(Large.get())
    cob= float(Lab.get())
    cofi= float(Fil.get())
    uni= float(uniform.get())
    codr= float(tution.get())

    sports_fee = cof*1
    largefee = coll*1
    labfee = cob*1
    costfiler = cofi*1
    uniformfeee = uni*1
    tutionfee = codr*1

    costpay = "Rs.",str('%.2f'% (sports_fee +  largefee + labfee + costfiler + uniformfeee + tutionfee))
    PayTax=((sports_fee +  largefee + labfee + costfiler +  uniformfeee + tutionfee)*0.33)
    Totalcost=(sports_fee +  largefee + labfee + costfiler  + uniformfeee + tutionfee)
    Ser_Charge=((sports_fee +  largefee + labfee + costfiler + uniformfeee + tutionfee)/100)
    Service="Rs.",str('%.2f'% Ser_Charge)
    OverAllCost="Rs.",str( round(PayTax + Totalcost + Ser_Charge,2))
    PaidTax="Rs.",str('%.2f'% PayTax)

    Service_Charge.set(Service)
    cost.set(costpay)
    Tax.set(PaidTax)
    Subtotal.set(costpay)
    Total.set(OverAllCost)


def qexit():
    root.destroy()

def reset():
    rand.set("")
    sports.set("")
    Large.set("")
    Lab.set("")
    Fil.set("")
    Subtotal.set("")
    Total.set("")
    Service_Charge.set("")
    tution.set("")
    Tax.set("")
    cost.set("")
    uniform.set("")


#---------------------------------------------------------------------------------------
rand = StringVar()
sports = StringVar()
Large = StringVar()
Lab = StringVar()
Fil = StringVar()
Subtotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
tution = StringVar()
Tax = StringVar()
cost = StringVar()
name = StringVar()
uniform = StringVar()


lblreference = Label(f1, font=( 'aria' ,16, 'bold' ),text="Admission No.",fg="brown",bd=20,anchor='w')
lblreference.grid(row=0,column=0)
txtreference = Entry(f1,font=('ariel' ,16,'bold'), textvariable=rand , bd=6,insertwidth=6,bg="yellow" ,justify='right')
txtreference.grid(row=0,column=1)


lbsports = Label(f1, font=( 'aria' ,16, 'bold' ),text=" Sports Fee ",fg="blue",bd=10,anchor='w')
lbsports.grid(row=2,column=0)
txtsports = Entry(f1,font=('ariel' ,16,'bold'), textvariable=sports , bd=6,insertwidth=4,bg="green" ,justify='right')
txtsports.grid(row=2,column=1)

lbllib = Label(f1, font=( 'aria' ,16, 'bold' ),text=" Library Fee ",fg="blue",bd=10,anchor='w')
lbllib.grid(row=3,column=0)
txtlib = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Large , bd=6,insertwidth=4,bg="green" ,justify='right')
txtlib.grid(row=3,column=1)


lbllab = Label(f1, font=( 'aria' ,16, 'bold' ),text="Lab Fee ",fg="blue",bd=10,anchor='w')
lbllab.grid(row=4,column=0)
txtlab = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Lab , bd=6,insertwidth=4,bg="green" ,justify='right')
txtlab.grid(row=4,column=1)

lblbus = Label(f1, font=( 'aria' ,16, 'bold' ),text="Bus Fee ",fg="blue",bd=10,anchor='w')
lblbus.grid(row=5,column=0)
txtbus = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Fil , bd=6,insertwidth=4,bg="green" ,justify='right')
txtbus.grid(row=5,column=1)

lbluniform = Label(f1, font=( 'aria' ,16, 'bold' ),text="Uniform Fee",fg="blue",bd=10,anchor='w')
lbluniform.grid(row=6,column=0)
txtuniform = Entry(f1,font=('ariel' ,16,'bold'), textvariable=uniform , bd=6,insertwidth=4,bg="green" ,justify='right')
txtuniform.grid(row=6,column=1)

#--------------------------------------------------------------------------------------
lbltution = Label(f1, font=( 'aria' ,16, 'bold' ),text="Tution Fee",fg="blue",bd=10,anchor='w')
lbltution.grid(row=1,column=0)
txttution = Entry(f1,font=('ariel' ,16,'bold'), textvariable=tution , bd=6,insertwidth=4,bg="green" ,justify='right')
txttution.grid(row=1,column=1)

lblstu = Label(f1, font=( 'aria' ,16, 'bold' ),text="Student Name",fg="black",bd=10,anchor='w')
lblstu.grid(row=1,column=2)
txtstu = Entry(f1,font=('ariel' ,16,'bold'), textvariable=name , bd=6,insertwidth=4,bg="yellow" ,justify='right')
txtstu.grid(row=1,column=3)

lblcost = Label(f1, font=( 'aria' ,16, 'bold' ),text="Cost",fg="black",bd=10,anchor='w')
lblcost.grid(row=2,column=2)
txtcost = Entry(f1,font=('ariel' ,16,'bold'), textvariable=cost , bd=6,insertwidth=4,bg="white" ,justify='right')
txtcost.grid(row=2,column=3)

lblService_Charge = Label(f1, font=( 'aria' ,16, 'bold' ),text="Service Charge",fg="black",bd=10,anchor='w')
lblService_Charge.grid(row=3,column=2)
txtService_Charge = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Service_Charge , bd=6,insertwidth=4,bg="white" ,justify='right')
txtService_Charge.grid(row=3,column=3)

lblTax = Label(f1, font=( 'aria' ,16, 'bold' ),text="Tax",fg="black",bd=10,anchor='w')
lblTax.grid(row=4,column=2)
txtTax = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Tax , bd=6,insertwidth=4,bg="white" ,justify='right')
txtTax.grid(row=4,column=3)

lblSubtotal = Label(f1, font=( 'aria' ,16, 'bold' ),text="Subtotal",fg="black",bd=10,anchor='w')
lblSubtotal.grid(row=5,column=2)
txtSubtotal = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Subtotal , bd=6,insertwidth=4,bg="white" ,justify='right')
txtSubtotal.grid(row=5,column=3)

lblTotal = Label(f1, font=( 'aria' ,16, 'bold' ),text="Total",fg="green",bd=10,anchor='w')
lblTotal.grid(row=6,column=2)
txtTotal = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Total , bd=6,insertwidth=4,bg="grey" ,justify='right')
txtTotal.grid(row=6,column=3)

#-----------------------------------------buttons------------------------------------------
lblTotal = Label(f1,text="---------------------",fg="white")
lblTotal.grid(row=7,columnspan=3)

btnTotal=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="TOTAL", bg="red",command=Ref)
btnTotal.grid(row=8, column=1)

btnreset=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="RESET", bg="red",command=reset)
btnreset.grid(row=8, column=2)

btnexit=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="EXIT", bg="red",command=qexit)
btnexit.grid(row=8, column=3)

def price():
    roo = Tk()
    roo.geometry("600x220+0+0")
    roo.title("Price List")
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="ITEM", fg="black", bd=5)
    lblinfo.grid(row=0, column=0)
    lblinfo = Label(roo, font=('aria', 15,'bold'), text="_____________", fg="white", anchor=W)
    lblinfo.grid(row=0, column=2)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="PRICE", fg="black", anchor=W)
    lblinfo.grid(row=0, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Tution Fee", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="25000", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Sports Fee ", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="1000", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Library Fee ", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="1500", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Lab Fee ", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="5000", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Bus Fee", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="12000", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Uniform Fee", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="4000", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=3)

    roo.mainloop()

btnprice=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="PRICE", bg="red",command=price)
btnprice.grid(row=8, column=0)

root.mainloop()

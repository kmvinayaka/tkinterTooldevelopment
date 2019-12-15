import datetime
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from tkinter import messagebox
import time
global fname, var1, var2, var3

def browse_file():
    global fname
    fname = filedialog.askopenfilename(filetypes = (("Template files", "*.py"), ("All files", ".py")))
    print (fname)

def genreport():
    global fname, var1, var2, var3
    if fname.split('.')[-1] == "py":
        print("test is performed ")
        info = tk.Label(master=back, text='Reports are getting generated').grid(row=6, sticky=W)
        #info5.update()
        c1 = 0;c2 = 0; c3 =0
        if var1.get() == 1:
            os.system('pylint '+fname+" > "+"pylint_"+os.path.split(fname)[-1].split(".")[-2]+"_"+datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")+".txt")
            print("running")

        if var2.get() == 1:
            os.system('bandit ' + fname + " > " + "bandit_" + os.path.split(fname)[-1].split(".")[-2]+"_"+ datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S") +".txt")

        if var3.get() == 1:
            os.system('radon cc ' + fname + "-a" + " > " + "radon_" + os.path.split(fname)[-1].split(".")[-2]+"_"+ datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S") +".txt")

        # if c1 or c2 or c3:
        #     info4 = tk.Label(master=back, text='reports are ready                        ').grid(row=6, sticky=W)



    else:
        print("Browse for .py")
        messagebox.showinfo("Browse for .py for tests")



mw = tk.Tk()

#If you have a large number of widgets, like it looks like you will for your
#game you can specify the attributes for all widgets simply like this.
#mw.option_add("*Button.Background", "white")
#mw.option_add("*Button.Foreground", "black")

mw.title('Tool for Test')
#You can set the geometry attribute to change the root windows size
mw.geometry("500x500") #You want the size of the app to be 500x500
mw.resizable(0, 0) #Don't allow resizing in the x or y direction

back = tk.Frame(master=mw)
back.pack_propagate(0) #Don't allow the widgets inside to determine the frame's width / height
back.pack(fill=tk.BOTH, expand=1) #Expand the frame to fill the root window

#Changed variables so you don't have these set to None from .pack()
go = tk.Button(master=back, text='Browse File', command=browse_file).grid(row=0, column = 1,sticky=W)
info = tk.Label(master=back, text='Select Tests').grid(row=1,sticky=W)

var1 = IntVar()
cb1 = tk.Checkbutton(master=back, text='Bandit for security issues ', variable=var1).grid(row=2, sticky=W)
#cb1.pack()
var2 = IntVar()
cb2 = tk.Checkbutton(master=back, text='Pylint for statistical issues', variable=var2).grid(row=3, sticky=W)
#cb2.pack()
var3 = IntVar()
print("kdgkldgfg",var3.get())
cb3 = tk.Checkbutton(master=back, text='Radon for cyclomatic complexity', variable=var3).grid(row=4, sticky=W)
#cb3.pack()
gen = tk.Button(master=back, text='generate report', command=genreport).grid(row=5, sticky=W)
close = tk.Button(master=back, text='Quit', command=mw.destroy).grid(row=10,column =1,sticky=W)


mw.mainloop()
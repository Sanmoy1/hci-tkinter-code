# after pressing a radio button on or off is displayed
from tkinter import *
from turtle import onclick
top=Tk()
top.geometry("400x400")
def onclick():
    label.config(text= f"Red lamp is {var.get()}")

var=StringVar(top,value="off")

label=Label(top,text="Red lamp is off")
label.grid(padx=2,pady=2)

radio1=Radiobutton(top,text="on",variable=var,value="on",command=onclick)
radio2=Radiobutton(top,text="off",variable=var,value="off",command=onclick)
radio1.grid(padx=3,pady=3)
radio2.grid(padx=3,pady=3)


top.mainloop()
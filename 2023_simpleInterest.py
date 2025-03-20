#simple interest calculator
from tkinter import *

top=Tk()
top.geometry("400x400")
top.title("Simple Interest Calculator")

def onclick():
    p=p_amt.get()
    r=rate.get()
    t=year.get()
    if(x.get()):
        ans=(float(p)*float(r)*float(t))/100
        answer.config(text=f"Simple interest is: {ans}")


name=Entry(top)
name.grid(padx=5,pady=5)
p_amt=Entry(top)
p_amt.grid(padx=5,pady=5)
rate=Entry(top)
rate.grid(padx=5,pady=5)
year=Entry(top)
year.grid(padx=5,pady=5)
x=BooleanVar()
confirm=Checkbutton(top,text="Confirm",variable=x)
confirm.grid(padx=5,pady=5)
btn=Button(top,text="Submit",command=onclick)
btn.grid(padx=5,pady=5)
answer=Label(top,text="The answer")
answer.grid(padx=5,pady=5)




top.mainloop()
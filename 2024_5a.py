from tkinter import *
import pandas as pd

def onclick():
    name_value = name.get()
    roll_no_value = roll_no.get()
    class_value = var.get()
    marks_value = marks.get()
    
    data = {
        "Name": [name_value],
        "Roll No": [roll_no_value],
        "Class": [class_value],
        "Marks": [marks_value]
    }
    
    df = pd.DataFrame(data)
    df.to_csv("text.csv", mode="a", header=not pd.io.common.file_exists("text.csv"), index=False)

top = Tk()
top.geometry("400x400")

name = Entry(top)
name.grid(padx=3, pady=3)

roll_no = Entry(top)
roll_no.grid(padx=3, pady=3)

values = ['1', '2', '3']
var = StringVar(value=values[0])
the_class = OptionMenu(top, var, *values)
the_class.grid(padx=3, pady=3)

marks = Scale(top, from_=0, to=100, orient=HORIZONTAL)
marks.grid(padx=3, pady=3)

btn = Button(top, text="Submit", command=onclick)
btn.grid(padx=3, pady=3)

top.mainloop()
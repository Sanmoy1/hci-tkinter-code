from tkinter import *
from tkinter import messagebox
class answer:
    def __init__(self,top):
        self.top=top
        self.top.geometry("500x500")
        self.para=Text(self.top,width=20,height=10)
        self.para.grid(padx=3,pady=3)
        self.editfield=Entry(self.top)
        self.editfield.grid(padx=3,pady=3)
        self.bt1=Button(self.top,text="Button 1",command=self.onclick1)
        self.bt2=Button(self.top,text="Button 2",command=self.onclick2)
        self.bt3=Button(self.top,text="Button 3",command=self.onclick3)
        self.bt4=Button(self.top,text="Button 4",command=self.onclick4)
        self.bt1.grid(padx=3,pady=3)
        self.bt2.grid(padx=3,pady=3)
        self.bt3.grid(padx=3,pady=3)
        self.bt4.grid(padx=3,pady=3)
        self.display=Label(self.top,text="The result is displayed")
        self.display.grid(padx=3,pady=3)
        
    def onclick1(self):
        para=self.para.get("1.0",END)
        para=para.split(".")
        self.display.config(text=para)
    def onclick2(self):
        para=self.para.get("1.0",END)
        para=para.split(" ")
        count=0
        for i in para:
            count+=1
        self.display.config(text=f"Count of words: {count}")
        uniqueWords=set(para)
        uniqueCount=len(uniqueWords)
        messagebox.showinfo("Unique words",f"Unique words: {uniqueCount}")

    def onclick3(self):
        editfield=self.editfield.get()
        para=self.para.get("1.0",END)
        para=para.split(" ")
        count=0
        for i in para:
            if editfield==i:
                count+=1
        self.display.config(text=f"Count of word {editfield} = {count}")
    def onclick4(self):
        para=self.para.get("1.0",END)
        para=para.split(" ")
        editfield=self.editfield.get()
        para.remove(editfield)
        self.display.config(text=" ".join(para))
    

top=Tk()
call=answer(top)
top.mainloop()


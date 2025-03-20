from calendar import isleap
from tkinter import *
top = Tk()
top.geometry("400x400")
story = Entry(top, width=50)
story.grid(padx=5, pady=20)


def onClickCount():
    theStory = story.get()
    #generic approach
    c = 0
    # for i in theStory:
    #     a = i.upper()
    #     if ord(a) >= 65 and ord(a) <= 90:
    #         c += 1
    #another good approach
    for i in theStory:
        if i.isalpha():
            c+=1
    ans.config(text=f"Number of Characters: {c}")


def onClickConvert():
    theStory=story.get()
    ans.config(text=f"Conversion result{theStory.upper()}")

def onClickErase():
    theStory=story.get()
    #this is the generic approach
    # s=""
    # for i in theStory:
    #     if(i.__eq__(" ")==False):
    #         s+=i
    # ans.config(text=f"{s}")
    #more optimized approach
    ans.config(text=theStory.replace(" ",""))

def onClickFind():
    theStory=story.get()+" "
    list=theStory.split(" ")
    s=""
    count=0
    for i in list:
        for j in list:
            if i==j:
                count+=1
        if count==1:
            s+=i+", "
        count=0
    ans.config(text=s)

count = Button(top, text="count", command=onClickCount)
count.grid(padx=5, pady=10)
convert = Button(top, text="convert", command=onClickConvert)
convert.grid(padx=5, pady=10)
erase = Button(top, text="erase", command=onClickErase)
erase.grid(padx=5, pady=10)
find = Button(top, text="find", command=onClickFind)
find.grid(padx=5, pady=10)
ans = Label(top, text="Display Answer")
ans.grid(padx=5, pady=10)
top.mainloop()

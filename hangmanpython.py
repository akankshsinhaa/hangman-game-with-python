import random
f=random.randint(0,4)
from tkinter import *
from tkinter import ttk
Main_window = Tk()

def tryGuess(string):
    ctr=0
    n=10
    if n>2:
        while ctr<n:
            x=string
            if x.isalpha():
             if x.lower()==secw.lower():
                return(("you won!"))
                break
             elif x!=secw:
                 for i in x:
                  if i in secw:
                     return(i)
                 ctr+=1
             else:
                ctr+=1
             if ctr==2:
                r=input("do you want a hint?: ").lower()
                if r=="y":
                    return(("%c") % (secw[0]))
            else:
                return(("Invalid input"))
        if ctr==n:
         return(("you lost!"))

tp=("apple","banana","orange","pears","pomegranate","kiwi")
secw=tp[f]
def display_text():
   global entry
   string= entry.get()
   
   label.configure(tryGuess(string))

label=Label(Main_window, text="", font=("Courier 22 bold"))
label.pack()

entry = Entry(Main_window, width=40)
entry.focus_set()
entry.pack()
ttk.Button(Main_window, text= "Try",width= 20, command= display_text).pack(pady=20)

Main_window.mainloop()




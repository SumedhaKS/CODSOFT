from tkinter import *
import tkinter.messagebox as msg
import random

root=Tk()

def Generate():
    try:
        len_val = int(len_entry.get())
        r = resources(len_val)
        display(r)

    except ValueError:
        msg.showinfo("It's Not a Number", " Please enter a valid number")

def resources(x):
    characters="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    num="0123456789"
    password=""
    for a in range(x):
        password+=random.choice(characters+num)
    return password

def display(p):
    ls.insert(END, p)

root.geometry('550x400')
root.title('Password Generator')


Len = Label(root, text="   Length of the Password:", font="Helvetica 10 bold")
Len.grid()

frame_1 = Frame(root, pady=10)
len_entry = Entry(frame_1, bd=3)
len_entry.grid(row=1,column=1)
frame_1.grid(row=1,column=1)

bt=Button(root, text="Submit", command=Generate)
bt.grid(row=2,column=1)
Label(root, text='').grid(row=3)

frame_2 =  Frame(root)
scrollbar = Scrollbar(frame_2)
scrollbar.pack(fill=Y,side=RIGHT)
frame_2.grid(row=5,column=2, sticky=N+S)

Label(root, text="Generated Password:", font="Helvetica 10 bold").grid(row=4)
ls = Listbox(root,  bd=3, yscrollcommand = scrollbar.set)
ls.grid(row=5, column=1)
scrollbar.config(command=ls.yview)

root.mainloop()

# Rock Paper Scissor Game

from tkinter import *
from PIL import Image, ImageTk
import random as rm
import time
import tkinter.messagebox as msg


root=Tk()

def restart():
    label_2.config(text="")
    but.destroy()


def rock():
    options=['Rock', 'Paper', 'Scissor']
    comp_choice = rm.choice(options)
    if comp_choice == 'Scissor':
        label_2.config(text="You chose: Rock\nComputer Chose: Scissor\nYou Win!")

    elif comp_choice == 'Paper':
        label_2.config(text="You chose: Rock\nComputer Chose: Paper\nYou Loose")

    else:
        label_2.config(text="You chose: Rock\nComputer Chose: Rock\nIt's a Draw")

    val = msg.askquestion("Play Again?", "Do you want to play again? ")
    if val == 'yes':
        global but
        but=Button(root, text="Restart", command=restart)
        but.pack()
    else:
        exit()


def paper():
    options=['Rock', 'Paper', 'Scissor']
    comp_choice = rm.choice(options)
    if comp_choice == 'Scissor':
        label_2.config(text="You chose: Paper\nComputer Chose: Scissor\nYou Loose")

    elif comp_choice == 'Rock':
        label_2.config(text="You chose: Paper\nComputer Chose: Rock\nYou Win!")

    else:
        label_2.config(text="You chose: Paper\nComputer Chose: Paper\nIt's a Draw")

    val = msg.askquestion("Play Again?", "Do you want to play again? ")
    if val == 'yes':
        global but
        but=Button(root, text="Restart", command=restart)
        but.pack()
    else:
        exit()

def scissor():
    options=['Rock', 'Paper', 'Scissor']
    comp_choice = rm.choice(options)
    if comp_choice == 'Scissor':
        label_2.config(text="You chose: Scissor\nComputer Chose: Paper\nYou Win!")

    elif comp_choice == 'Rock':
        label_2.config(text="You chose: Scissor\nComputer Chose: Rock\nYou Loose")

    else:
        label_2.config(text="You chose: Scissor\nComputer Chose: Scissor\nIt's a Draw")

    val = msg.askquestion("Play Again?", "Do you want to play again? ")
    if val == 'yes':
        global but
        but=Button(root, text="Restart", command=restart)
        but.pack()
    else:
        exit()


root.geometry('540x540')
root.title('Rock Paper Scissor')

label_1 = Label(root, text=" Pick One ", font='Castellar 15 bold', bg='PeachPuff4', fg='snow')
label_1.pack(side=TOP, fill="x")

image = Image.open("rps.jpg")
photo = ImageTk.PhotoImage(image)

img_label= Label(image=photo)
img_label.pack()

choice=StringVar()

frame_1=Frame(root)
Button(frame_1, text="Rock", padx=18, bd=5, command=rock).grid(row=10,column=1)
Button(frame_1, text="Paper", padx=15, bd=5, command=paper).grid(row=10,column=2)
Button(frame_1, text="Scissor", padx=15, bd=5, command=scissor).grid(row=10,column=3)
frame_1.pack()

frame_2=Frame(root)
label_2 = Label(frame_2, text='',font='Castellar 15 bold')
label_2.pack(side=TOP, fill="x")
frame_2.pack()



root.mainloop()

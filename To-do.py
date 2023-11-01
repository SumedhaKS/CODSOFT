# A GUI based TO-Do List

from tkinter import *

root=Tk()
root.geometry("800x550")
root.title("To-Do List")
Label(root,text='MAKE IT HAPPEN !' ,font='Helvetica 15 bold' ,
    borderwidth=10,padx=10,pady=10).grid(row=0,column=1)

#Function to add item to the listbox and also to store in a file
def add():
    var=inp_entry.get()
    with open('data.txt', 'a') as f:
        f.write(var)
        f.write('\n')

    lx.insert(END, var)
    inp_entry.delete(0, END)

#Funtion to delete an item from the listbox
def delete_item():
    index = lx.curselection()
    if index:
        index=int(index[0])
        item=lx.get(index)    #Here we are retrieving the item for deleting it from the file
        lx.delete(index)

    with open('data.txt','r') as f:
        lines=f.readlines()
    with open('data.txt','w') as f:
        for line in lines:
            if line.strip() != item:
                f.write(line)

def Clear_all():
    try:
        with open('data.txt', 'w') as f:
            lx.delete(0, END)
    except FileNotFoundError:
        print("File  not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

#Shows Content in the ListBox
def list_val():
    try:
        with open('data.txt','r') as f:
            lines=f.readlines()
            for line in lines:
                lx.insert(END, line.strip())
    except FileNotFoundError:
        with open('data.txt', 'w'):
            pass

#Creating Listbox
lx=Listbox(root, width=80, borderwidth=4 )
lx.grid(row=2,column=3)
list_val()

#Creating Scrollbar and linking it to the ListBox
sb = Scrollbar(root, orient=VERTICAL,command=lx.yview)
sb.grid(row=2,column=4,padx=5,pady=40, sticky=N+S )
lx.config(yscrollcommand=sb.set)

label=Label(root,text='Enter the Task:' ,font="Helvetica 10 italic bold" ,
    borderwidth=10,padx=7,pady=4).grid(row=3,column=3)

#Creating Entry Widget
ef=Frame(root, width=5,height=5, padx=5, pady=5)
inp_entry=Entry(ef ,width=25, borderwidth=5 )
inp_entry.grid()
ef.grid(row=4,column=3)

label=Label(root,text='' , borderwidth=10,padx=1,pady=1).grid(row=5,column=3)

#Creating Buttons
bt1=Button(root,text=" Add to list",padx=21,borderwidth=4, command=add ).grid(row=6,column=3)
bt2=Button(root,text="Delete from list",padx=10,borderwidth=4, command=delete_item).grid(row=7,column=3)
bt3=Button(root,text="Clear All",padx=28,borderwidth=4, command=Clear_all).grid(row=8,column=3)

root.mainloop()

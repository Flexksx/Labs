import random
from tkinter import *

# Greeting stuff
colors = ['Red', 'Green', 'Yellow', 'Purple', 'Blue', 'Cyan']

window = Tk()
spinsize = 10
window.geometry("700x700")
window.title("MastermindFUCK")
greetinglabel = Label(window, text="Try to break the code! There are 6 possible colors.", font=("Bahnschrift", 20),
                      padx=50, pady=10)
greetinglabel.grid(column=0, row=0)


# Greeting stuff

# Player input

def getbox1():
    global box1
    box1=StringVar()
    box1=Spinbox.get()

def getbox2():
    global box2
    box2= StringVar()
    box2=Spinbox.get()

def getbox3():
    global box3
    box3= StringVar()
    box3=Spinbox.get()

def getbox4():
    global box4
    box4 = StringVar()
    box4=Spinbox.get()


tryframes = []
for i in range(12):
    tryframes.append(Frame(window))
    tryframes[i].grid(column=0, row=i + 2)

inputframe = Frame(window)
inputframe.grid(column=0, row=1)
spinbox1 = Spinbox(inputframe, values=colors, font=("Bahnschrift", spinsize), command=getbox1()).pack(side=RIGHT)
spinbox2 = Spinbox(inputframe, values=colors, font=("Bahnschrift", spinsize), command=getbox2()).pack(side=RIGHT)
spinbox3 = Spinbox(inputframe, values=colors, font=("Bahnschrift", spinsize), command=getbox3()).pack(side=RIGHT)
spinbox4 = Spinbox(inputframe, values=colors, font=("Bahnschrift", spinsize), command=getbox4()).pack(side=RIGHT)

trybutton = Button(inputframe, text="TRY!", font=("Bahnschrift", spinsize)).pack(side=LEFT)

# Player input


window.mainloop()


def getcode(colors):
    return random.choices(colors, k=4)


code = getcode(colors)


def givepins(code, x):
    pins = []
    pos = []
    for i in range(len(x)):
        if x[i] == code[i]:
            pins.append('R')
            x[i] = 'X'
    x = list(x)
    for i in x:
        if i in code:
            pins.append('W')
            i = 'X'
    print(x)
    return pins


print(code)

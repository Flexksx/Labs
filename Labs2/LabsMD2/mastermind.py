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

global box1
global box2
global box3
global box4
def getvals():
    box1=spinbox1.get()
    box2=spinbox2.get()
    box3=spinbox3.get()
    box4=spinbox4.get()
    print(box1,box2,box3,box4)

tryframes = []
for i in range(12):
    tryframes.append(Frame(window))
    tryframes[i].grid(column=0, row=i + 2)

inputframe = Frame(window)
inputframe.grid(column=0, row=1)
spinbox1 = Spinbox(inputframe, values=colors, font=("Bahnschrift", spinsize)).pack(side=RIGHT)
spinbox2 = Spinbox(inputframe, values=colors, font=("Bahnschrift", spinsize)).pack(side=RIGHT)
spinbox3 = Spinbox(inputframe, values=colors, font=("Bahnschrift", spinsize)).pack(side=RIGHT)
spinbox4 = Spinbox(inputframe, values=colors, font=("Bahnschrift", spinsize)).pack(side=RIGHT)

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

import random
from tkinter import *
from tkinter import ttk

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



tryframes = []
for i in range(12):
    tryframes.append(Frame(window))
    tryframes[i].grid(column=0, row=i + 2)


box1 = Spinbox(window, values=colors, font=("Bahnschrift", spinsize), wrap=True)
box1.grid(column=0,row=1)
box2 = Spinbox(window, values=colors, font=("Bahnschrift", spinsize), wrap=True)
box2.grid(column=1,row=1)
box3 = Spinbox(window, values=colors, font=("Bahnschrift", spinsize), wrap=True)
box3.grid(column=2,row=1)
box4 = Spinbox(window, values=colors, font=("Bahnschrift", spinsize), wrap=True)
box4.grid(column=3,row=1)

def printvals():
    vals=[]
    vals.append(box1.get())
    vals.append(box2.get())
    vals.append(box3.get())
    vals.append(box4.get())
    print(vals)

trybutton = Button(window, text="TRY!", font=("Bahnschrift", spinsize), command=lambda: printvals())
trybutton.grid(column=4,row=1)


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

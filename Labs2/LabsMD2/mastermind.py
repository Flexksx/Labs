import random
from tkinter import *

window = Tk()
colors = ['Red', 'Green', 'Yellow', 'Purple', 'Blue', 'Cyan']
code = random.choices(colors, k=4)
spinsize = 10
window.geometry("700x700")
window.title("MastermindFUCK")
greetingframe = Frame(window)
greetinglabel = Label(greetingframe, text="Try to break the code! There are 6 possible colors.", font=("Bahnschrift", 20)).pack()
tryframes = []
box1 = Spinbox(window, values=colors, font=("Bahnschrift", spinsize), wrap=True)
box1.grid(column=0, row=1)
box2 = Spinbox(window, values=colors, font=("Bahnschrift", spinsize), wrap=True)
box2.grid(column=1, row=1)
box3 = Spinbox(window, values=colors, font=("Bahnschrift", spinsize), wrap=True)
box3.grid(column=2, row=1)
box4 = Spinbox(window, values=colors, font=("Bahnschrift", spinsize), wrap=True)
box4.grid(column=3, row=1)

print(code)


def getvals():
    vals = []
    vals.append(box1.get())
    vals.append(box2.get())
    vals.append(box3.get())
    vals.append(box4.get())
    return vals


def givepins(tempcode, ans):
    pins = []
    for i in range(len(ans)):
        pins.append('Black')
    for i in range(len(ans)):
        if ans[i] == tempcode[i]:
            pins.remove('Black')
            pins.append('Red')
    return pins

tries=0
def inc(value):
    global tries
    tries += value

def check(tries):
    vals = getvals()
    result = givepins(code, vals)
    print(result)
    tryframes.append(Frame(window))
    tryframes[tries].grid(column=0, row=tries + 2)
    for j in range(0, 4):
        tryframes[tries][j] = Label(tryframes[tries], text='O', fg=result[j], font=("Bahnschrift", 10)).pack(side=LEFT)
    tries += 1
    print(tries)


trybutton = Button(window, text="TRY!", font=("Bahnschrift", spinsize), command=lambda: [check(tries), inc(1)])
trybutton.grid(column=4, row=1)

window.mainloop()

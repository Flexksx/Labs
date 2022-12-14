import random
from tkinter import *

window = Tk()
colors = ['Red', 'Green', 'Yellow', 'Purple', 'Blue', 'Cyan']
code = random.choices(colors, k=4)
spinsize = 10
window.geometry("700x700")
window.title("MastermindFUCK")
greetingframe = Frame(window)
greetinglabel = Label(greetingframe, text="Try to break the code! There are 6 possible colors.",
                      font=("Bahnschrift", 20)).pack()
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


def givepins(code, ans):
    pins = []
    tempcode=code
    count=0
    for i in range(len(ans)):
        pins.append('Black')
    for i in range(len(ans)):
        if ans[i] == tempcode[i]:
            pins.remove('Black')
            pins.append('Red')
    for  i in range(len(ans)):
            if ans[i] in tempcode and not ans[i]==tempcode[i]:
                count+=1
    for i in range(count):
        pins.append('Yellow')
        pins.remove('Black')
    return pins


tries = 0
winframe=Frame(window)

def inc(value):
    global tries
    tries += value


def check(tries):
    vals = getvals()
    result = givepins(code, vals)
    tryframes.append(Frame(window))
    tryframes[tries].grid(column=0, row=tries + 2, columnspan=4)
    for j in range(0, 4):
        tryframes[tries][j] = Label(tryframes[tries], text='O', fg=result[j], font=("Bahnschrift", 20)).pack(side=LEFT)
    tryframes[tries][5] = Label(tryframes[tries], text='Previous try: ', font=("Bahnschrift", 20)).pack(side=LEFT)
    for j in range(6,10):
        tryframes[tries][j] = Label(tryframes[tries], text='O', fg=vals[j-6], font=("Bahnschrift", 20)).pack(side=LEFT)
    tries += 1
    if result == ['Red', 'Red', 'Red', 'Red']:
        global winframe
        winframe.grid(column=0, row=tries+3, columnspan=4)
        winlabel=Label(winframe, text="Conratulations! You won!", font=("Bahnschrift", 30)).pack()
        playagain=Button(winframe, text="Play again!", font=("Bahnschrift", 20), command=lambda: newgame()).pack(side=LEFT)


def newgame():
    global tries
    global tryframes
    for i in  range(tries):
        tryframes[i].destroy()
    global code
    code = random.choices(colors, k=4)
    global winframe
    winframe.destroy()
    print(code)

trybutton = Button(window, text="TRY!", font=("Bahnschrift", spinsize), command=lambda: [check(tries), inc(1)])

trybutton.grid(column=4, row=1)

window.mainloop()

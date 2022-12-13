import random
from tkinter import *

window=Tk()
window.geometry("500x300")
window.title("Mastermind")
label1=Label(window, text="Guess the number!", font=("Times New Roman",32), padx=80)
label1.grid(column=0, row=0)
labelnum = Label(window, text="XXXX", font=("Times New Roman", 24), padx=100, pady=100)
labelnum.grid(column=0, row=1)
window.mainloop()


num = str(random.randint(1000,9999))
def getblank(num):
    show=[]
    for i in range(len(num)):
        show.append('X')
    return ''.join(show)

show=getblank(num)

gamegoing=True
steps=0
print(num)
while gamegoing:
    show=getblank(num)
    x = input()
    for i in range(len(x)):
        if num[i]==x[i]:
            show=list(show)
            show[i]=num[i]
            show=''.join(show)
    print(show)

    steps+=1
    if show==num:
        print("You won in", steps,"steps!")
        gamegoing=False
    if x=='stop':
        gamegoing=False





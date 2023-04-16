from tkinter import *

# window=Tk()
# window.geometry("500x300")
# window.title("Sugmalator")
# NameFrame=Frame(window)
# NameFrameLabel=Label(NameFrame, text="Kizda messi", font=("Bahnschrift",20)).pack()

def DecMinus(a:str,b:str):
    if len(a)>=len(b):
        size=len(b)
    else:
        size=len(a)
        temp=a
        a=b
        b=temp
    for i in range(size,0,-1):
        print(b[i])


DecMinus('123','12')


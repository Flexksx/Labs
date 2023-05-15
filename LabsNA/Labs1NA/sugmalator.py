from tkinter import *

# window=Tk()
# window.geometry("500x300")
# window.title("Sugmalator")
# NameFrame=Frame(window)
# NameFrameLabel=Label(NameFrame, text="Kizda messi", font=("Bahnschrift",20)).pack()




def DecMinusInt(a:str, b:str):
    #Find which is greater
    sign='+'
    if len(b)>len(a):
        temp=a
        a=b
        b=temp
        sign='-'
    a.split()
    b.split()
    la=len(a)
    lb=len(b)
    dl=la-lb
    res=[a[i] for i in range(la)]
    # print(a,b,sign,la,lb,dl)
    for i in range(0,lb):
        dig1=int(a[la-i-1])
        dig2=int(b[lb-i-1])
        # print(dig1,dig2)
        res[la-i-1]=str(abs(dig1-dig2))
    return sign+''.join(res)



print(DecMinus("212","12"))        
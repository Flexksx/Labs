def xnor(a,b):
    if(a=='1' or a=="True"):
        a=True
    elif(a=='0' or a=="False"):
        a=False
    if(b=='1' or b=="True"):
        b=True
    elif(b=='0' or b=="False"):
        b=False
    c=((a and b) or ((not a) and (not b)))
    print(c)
    
a=input()
b=input()
xnor(a,b)

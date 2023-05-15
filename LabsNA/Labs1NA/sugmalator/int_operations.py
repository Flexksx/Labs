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
    dl=len(a)-len(b)
    res=[a[i] for i in range(len(a))]
    # print(a,b,sign,len(a),len(b),dl)
    for i in range(0,len(b)):
        dig1=int(a[len(a)-i-1])
        dig2=int(b[len(b)-i-1])
        # print(dig1,dig2)
        res[len(a)-i-1]=str(abs(dig1-dig2))
    return sign+''.join(res)

def DecPlusInt(a:str, b:str):
    la=len(a)
    lb=len(b)
    if len(b)>len(a):
        temp=a
        a=b
        b=temp
    a.split()
    b.split()
    res=[]
    for i in range(0,lb):
        print('hi')


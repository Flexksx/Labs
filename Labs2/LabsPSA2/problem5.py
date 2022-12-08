import random

def coi():
    ans=[]
    b=random.uniform(-1,1)
    c=random.uniform(-1,1)
    if (pow(b,2)-4*c)<0:
        ans.append("Complex")
    else:
        ans.append("Real")
    x1=(-b+pow((pow(b,2)-4*c),0.5))/2
    x2=(-b-pow((pow(b,2)-4*c),0.5))/2
    if x1>0 and x2>0 and ans[0]=="Real":
        ans.append("Positive")
    else:
        ans.append("Negative")
    print(ans)
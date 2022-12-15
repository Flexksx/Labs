import random

def game():
    x=random.uniform(0,1)
    y=random.uniform(0,1)
    i=1
    while y<x:
        y=random.uniform(0,1)
        i+=1
    return i-1


money=0
tries=1000000
for i in range(tries):
    money+=game()

print(money/tries)
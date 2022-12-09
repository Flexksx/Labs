import random


def circleCenter():
    return [random.uniform(0, 16), random.uniform(0, 16)]


def distance(x1, y1, x2, y2):
    return pow(((x2 - x1) ** 2) + ((y2 - y1) ** 2), 0.5)

money=0
tries=1
prob=0
for i in range(tries):
    circle = circleCenter()
    x = int(circle[0])
    y = int(circle[1])
    print(x,y)
    if x % 2 == 0 and x > 1:
        if circle[0]-x>0:
            x+=1
        else:
            x-=1
    if y % 2 == 0 and y > 1:
        if circle[1] - y > 0:
            y += 1
        else:
            y -= 1
    square = [x, y]
    if abs(square[0] - circle[0]) < 0.5 and abs(square[1] - circle[1]) < 0.5:
        money += 1
        prob+=1
    else:
        money -= 0.25
    print(circle)
    print(square)


print(money)
import turtle as t

t.speed(0)


def sierpinski(size, d):
    if d == 0:
        for i in range(0, 3):
            t.fd(size)
            t.lt(120)
    else:
        sierpinski(size / 2, d - 1)
        t.fd(size / 2)
        sierpinski(size / 2, d - 1)
        t.bk(size / 2)
        t.lt(60)
        t.fd(size / 2)
        t.rt(60)
        sierpinski(size / 2, d - 1)
        t.lt(60)
        t.bk(size / 2)
        t.rt(60)


d = int(input())
sierpinski(400, d)
t.Screen().exitonclick()

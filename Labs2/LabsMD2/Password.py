def lower(a):
    for i in range(len(a)):
        if a[i] in "abcdefghijklmnopqrstuvwxyz":
            return True
        else:
            flag = 0
    if flag == 0:
        return False


def upper(a):
    for i in range(len(a)):
        if a[i] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            return True
        else:
            flag = 0
    if flag == 0:
        return False


def digit(a):
    for i in range(len(a)):
        if a[i] in "1234567890":
            return True
        else:
            flag = 0
    if flag == 0:
        return False


def symbol(a):
    for i in range(len(a)):
        if a[i] in "~`!@#$%^&*()-_+={}[]|\;:""<>,./?":
            return True
        else:
            flag = 0
    if flag == 0:
        return False


def repeating(a):
    for i in range(len(a) - 2):
        if a[i] == a[i + 1] == a[i + 2]:
            return False
    return True


def countrepeat(a):
    a = list(a)
    count = 0
    for i in range(len(a) - 2):
        if a[i] == a[i + 1] == a[i + 2]:
            count += 1
            if count > 0:
                a[i] = a[i + 1] = a[i + 2] = ""
    return count


password = input()


steps = 0
if not lower(password):
    steps += 1
if not upper(password):
    steps += 1
if not digit(password):
    steps += 1
if not symbol(password):
    steps += 1
if not repeating(password):
    if steps > 0 and steps >= countrepeat(password):
        steps = steps
    elif countrepeat(password) > steps > 0:
        steps = countrepeat(password)
    else:
        steps += countrepeat(password)


if len(password) < 8:
    if steps > 0:
        if steps >= 8 - len(password):
            steps = steps
        else:
            steps = 8 - len(password)
    else:
        steps = 8 - len(password)
elif len(password) > 20:
    password1 = password[0:20]
    steps1 = 0
    if not lower(password1):
        steps1 += 1
    if not upper(password1):
        steps1 += 1
    if not digit(password1):
        steps1 += 1
    if not symbol(password1):
        steps1 += 1
    if not repeating(password1):
        if steps1 > 0 and steps1 >= countrepeat(password1):
            steps1 = steps1
        elif countrepeat(password1) > steps1 > 0:
            steps1 = countrepeat(password1)
        else:
            steps1 += countrepeat(password1)
    if steps1 > 0:
        if steps1 >= len(password) - 20:
            steps = steps1
        else:
            steps =steps1 + len(password) - 20
    else:
        steps = len(password) - 20
if steps != 0:
    print(steps)
else:
    print("good")

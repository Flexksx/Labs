def lowercase(a):
    for i in range(len(a)):
        if a[i] in "abcdefghijklmnopqrstuvwxyz":
            return True
        else:
            flag = 0
    if flag == 0:
        return False


def uppercase(a):
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


def length(a):
    if len(a) < 8:
        return 8 - len(a)
    elif len(a) > 20:
        return len(a) - 25
    else:
        return True


def removerepeats(a):
    a = list(a)
    for i in range(len(a) - 3):
        if a[i] == a[i + 1] == a[i + 2]:
            a.remove(a[i + 2])

    return ''.join(a)


password = "pulaaaa"
# print(lowercase(password))
# print(uppercase(password))
# print(digit(password))
# print(symbol(password))
# print(repeating(password))
# print(length(password))

steps = 0
if not lowercase(password):
    steps += 1
if not uppercase(password):
    steps += 1
if not digit(password):
    steps += 1
if not symbol(password):
    steps += 1
if repeating(password):
    print("Hi")

print(removerepeats(password))

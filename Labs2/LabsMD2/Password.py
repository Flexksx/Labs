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


def countrepeats(a):
    a = list(a)
    count = 0
    for i in range(len(a) - 2):
        if a[i] == a[i + 1] == a[i + 2]:
            count += 1
    return count


password = input()
# print(lowercase(password))
# print(uppercase(password))
# print(digit(password))
# print(symbol(password))
# print(repeating(password))
# print(length(password))

steps = 0

if len(password) < 8:
    print(abs(8-len(password)))
    exit()
elif len(password) > 20:
    print(abs(20-len(password)))
    exit()
if not lowercase(password):
    steps += 1
if not uppercase(password):
    steps += 1
if not digit(password):
    steps += 1
if not symbol(password):
    steps += 1
if not repeating(password):
    steps += countrepeats(password)

if steps!=0:
    print(steps)
else:
    print("G00D")

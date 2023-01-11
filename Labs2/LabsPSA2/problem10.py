import random

jora = 0
troleibuz = 6
days = 365
fines = 0


def controlor():
    x = random.uniform(0, 1)
    if x <= 0.05:
        return True
    else:
        return False


def ricardo():
    x = random.uniform(0, 1)
    if x <= 0.02:
        return True
    else:
        return False


for i in range(days * 2):
    if not ricardo():
        if controlor():
            if fines == 0:
                jora += 50
            elif fines == 1:
                jora += 150
            elif fines > 1:
                jora += 300
        fines += 1
    elif ricardo():
        jora += troleibuz

print("Being honest costs you", days * 2 * troleibuz, ",while being Jora costs you", jora)
if jora > days * 2 * troleibuz:
    print("Just pay the ticket")

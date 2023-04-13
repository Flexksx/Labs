import random


def revolveradj(bllt, chmb):
    pist = []
    for i in range(chmb):
        pist.append(0)
    load = random.randint(1, chmb)
    if load == chmb:
        pist[0] = 1
        pist[chmb - 1] = 1
    elif load != chmb:
        pist[load - 1] = 1
        pist[load] = 1
    return pist


def revolvernonadj(bllt, chmb):
    pist = []
    for i in range(chmb):
        pist.append(0)
    load1 = random.randint(1, chmb)
    if (load1 == chmb):
        pist[load1 - 1] = 1
    else:
        pist[load1] = 1
    load2 = random.randint(1, chmb)
    if (load2 == load1 or load2==load1+1 or load2==load1-1 or (load2==1 and load1==chmb)):
        while (load2 == load1 or load2==load1+1 or load2==load1-1 or (load2==1 and load1==chmb)):
            load2 = random.randint(1, chmb)
    if (load2 == chmb):
        pist[load2 - 1] = 1
    else:
        pist[load2] = 1
    return pist


def spin(bullets, chambs, tries, pist):
    deaths = 0
    for i in range(tries):
        pick = random.randint(0, chambs - 1)
        if (pist[pick] == 1):
            deaths = deaths + 1
    return 1 - (deaths / tries)


def nospin(bullets, chambs, tries, pist):
    deaths = 0
    discounttries = 0
    for i in range(tries):
        pick = random.randint(0, chambs - 1)
        if (pist[pick] == 0):
            if (pick == chambs - 1):
                if (pist[0] == 1):
                    deaths += 1
            else:
                if (pist[pick + 1] == 1):
                    deaths += 1
        elif (pist[pick] == 1):
            discounttries += 1
    return 1 - deaths / (tries - discounttries)


def spinadj(bullets, chambs, tries):
    pist = revolveradj(bullets, chambs)
    return spin(bullets, chambs, tries, pist)


def nospinadj(bullets, chambs, tries):
    pist = revolveradj(bullets, chambs)
    return nospin(bullets, chambs, tries, pist)


def spinnadj(bullets, chambs, tries):
    pist = revolvernonadj(bullets, chambs)
    return spin(bullets, chambs, tries, pist)


def nospinnadj(bullets, chambs, tries):
    pist = revolvernonadj(bullets, chambs)
    return nospin(bullets, chambs, tries, pist)


def printadj(a, b, tries):
    print("spin,", a, "adjacent bullets in", b, "chambers: ", spinadj(a, b, tries))
    print("no spin,", a, "adjacent bullets in", b, "chambers: ", nospinadj(a, b, tries))


def printnonadj(a, b, tries):
    print("spin", a, "bullets in", b, "chambers: ", nospinnadj(a, b, tries))
    print("no spin", a, "bullets in", b, "chambers: ", spinnadj(a, b, tries))


tries = 10000
printadj(2, 6, tries)
printadj(2, 5, tries)
printnonadj(2, 6, tries)
printnonadj(2, 5, tries)

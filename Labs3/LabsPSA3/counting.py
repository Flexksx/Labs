import random

people = [i for i in range(100)]


def seated(a):
    for x in a:
        if a[x] == False:
            return False
    return True

def simulation(people):
    seats = {}
    for i in people:
        seats.update({i: False})
    first = random.randint(0, 99)
    seats[0] = first
    index = 0
    while not seated(seats):
        for x in seats:
            if x == index:
                continue
            else:
                seats[x] = x
            if x == first:
                first = random.randint(0,99)
                index = x
                break
        print(seats)
    return seats


print(simulation(people))

import random

n = 10
participants = []

for i in range(n):
    participants.append(str(i))


def seats(people, n):
    sequence = []
    while len(sequence) < n:
        x = random.randint(0, n - 1)
        if people[x] not in sequence:
            sequence.append(people[x])
    return sequence


def compare(people, n):
    lunch = seats(people, n)
    dinner = seats(people, n)
    print(lunch)
    print(dinner)


compare(participants, n)

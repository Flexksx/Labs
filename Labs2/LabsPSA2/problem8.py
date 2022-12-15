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
    for j in range(n):
        if dinner[j] == lunch[n - 1] and dinner[j] == lunch[0]:
            return 0
    for j in range(1, n - 1):
        for q in range(1, n - 1):
            if not j == q and lunch[j] == dinner[q]:
                if lunch[j + 1] == dinner[q + 1] or lunch[j - 1] == dinner[q - 1]:
                    return 0
    return 1


prob = 0
tries = 1000
for i in range(tries):
    prob += compare(participants, n)

print(prob / tries)

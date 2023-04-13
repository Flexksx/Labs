import random

est = (50 * 200) / 8
print('Estimation:' + str(est))
prob = 0.04
deer = 0
tries = 1000

for i in range(tries):
    flag = 0
    while flag < 50:
        deer += 1
        if random.uniform(0, 1) <= prob:
            flag += 1

print('Simulation:' + str(deer / tries))

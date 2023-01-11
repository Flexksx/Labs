nr = int(input('Nr:'))
begin = int(input('Start:'))
end = int(input('Stop:'))
k = int(input('MaxStops:'))
flights = [[0]*3]*nr


def cheapest_route(fl, st, dest, k):
    if st == dest:
        return [0, []]
    if k < 0:
        return [float('inf'), []]
    cost = float('inf')
    temp = []
    for i in fl:
        if i[0] == st:
            poi = cheapest_route(fl, i[1], dest, k-1)
            new_cost = i[2] + poi[0]
            if cost > new_cost:
                cost = new_cost
                if len(temp) > 1:
                    temp.pop()
                    temp.pop()
                temp.append(i[1])
                for w in poi[1]:
                    temp.append(w)
    if cost == float('inf'):
        return [float('inf'), []]
    else:

        return [cost, temp]


for q in range(nr):
    flights[q] = [int(x) for x in input().split()]
ans = cheapest_route(flights, begin, end, k)


print('cost',ans[0])
print('route',ans[1])
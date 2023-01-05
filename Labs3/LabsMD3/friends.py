with open('resources\\matrix.txt', 'r') as f:
    matrix = f.read()
matrix = matrix.split()
people = [(matrix[i] + ' ' + matrix[i + 1]) if matrix[i] != '|' else '' for i in range(0, 60, 3)]


def getgraph(people, matrix):
    for i in matrix:
        if i == '|':
            matrix.remove(i)
    ans = {}
    q = 0
    for i in range(42, len(matrix), 22):
        friends = []
        vals = matrix[i:i + 20]
        for j in range(len(vals)):
            if vals[j] == '1':
                friends.append(people[j])
        ans.update({people[q]: friends})
        q += 1
    return ans


graph = getgraph(people, matrix)


def mostfriends(network):
    maxlen = 0
    ans = ''
    for x in network:
        if len(network[x]) > maxlen:
            maxlen = len(network[x])
            ans = x
    return ans


def sortbyfriends(network):
    ans = {}
    while network != {}:
        max = 0
        name = ''
        for x in network:
            if len(network[x]) > max:
                max = len(network[x])
                name = x
        ans.update({name: network[name]})
        del network[name]
    return dict(reversed(list(ans.items())))


def witcher(start,stop,network):



print(mostfriends(graph))
print(sortbyfriends(graph))

import sys

with open('C:\\Users\\Cristi\\Documents\\GitHub\\Labs\\Labs3\\LabsMD3\\resources\\matrix.txt', 'r') as f:
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


def adjmat(matstr):
    ans = [[0 for i in range(20)] for j in range(20)]
    q = 0
    for i in range(42, len(matstr), 22):
        vals = matstr[i:i + 20]
        for j in range(0, len(vals) - 1):
            ans[q][j] = vals[j]
        q += 1
    return ans


def ratings(net):
    def dijkstra(net, start, end):
        distances = {node: sys.maxsize for node in net}
        distances[start] = 0
        unvisited_nodes = set(net.keys())
        while unvisited_nodes:
            current_node = min(unvisited_nodes, key=lambda node: distances[node])
            unvisited_nodes.remove(current_node)
            if current_node == end:
                break
            for neighbor in net[current_node]:
                new_distance = distances[current_node] + 1
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance

        return distances

    def distancematrix(net):
        nodes = list(net.keys())
        ans = [[0 for i in range(20)] for j in range(20)]
        for x in net:
            for y in net:
                if x != y:
                    distances = dijkstra(net, x, y)
                    ans[nodes.index(x)][nodes.index(y)] = distances[y]
        return ans

    def giveratings():
        rating_matrix = distancematrix(net)
        people = list(net.keys())
        rating_dict = {}
        for i in range(len(rating_matrix)):
            ratingsum = 0
            for j in range(len(rating_matrix[i])):
                ratingsum += rating_matrix[i][j]
            rating_dict.update({people[i]: ratingsum})
        return rating_dict

    def answer():
        names = giveratings()
        names = sorted(names.items(), key=lambda x: x[1])
        ans = {}
        for i in names:
            ans.update({i[0]: i[1]})
        return ans

    return answer()


def newrating(net):
    with open("resources\\influence.txt", 'r') as f:
        txt = f.read().split()
    freq = {}
    for i in range(0, len(txt), 4):
        freq.update({txt[i] + " " + txt[i + 1]: float(txt[i + 3])})
    ans = ratings(net)
    for x in freq:
        ans[x] = ans[x] * (freq[x] * 0.5)

    names = sorted(ans.items(), key=lambda x: x[1])
    ans = {}
    for i in names:
        ans.update({i[0]: i[1]})
    return ans


def market():
    with open("resources\\interests.txt", 'r') as f:
        interests = f.read().split()
    title = "From T-Rex to Multi Universes: How the Internet has Changed Politics, Art and Cute Cats"
    ans = []
    for i in interests:
        if i in title:
            ans.append(i)
    return ans


def promotion(net):
    with open("resources\\people_interests.txt", 'r') as f:
        txt = f.read().strip().split()
    people = list(net.keys())
    ratings = newrating(net)
    ans = {}
    h = 0
    start = 0
    end = 0
    for i in range(0, len(txt) - 1):
        if txt[i] == ":":
            start = i
            for j in range(start, len(txt) - 1):
                if txt[j] == ":" and j > start:
                    end = j
                    break
            interests = list(set(txt[start + 1:end - 2]))
            ans.update({people[h]: interests})
            h += 1
    ans.update({people[len(people)-1]:[str(txt[-2]), str(txt[-1])]})
    print(ans)


# print(mostfriends(graph))
# print(sortbyfriends(graph))
# print(ratings(graph))
# print(newrating(graph))
# print(market())
promotion(graph)

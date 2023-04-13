total_courses = int(input())
prerequisites = [[0]*2]*total_courses
visited = {int(x) for x in range(total_courses)}
verify, minus = list(), list()
visited_list = []
def search(graph, viz):
    for k in range(total_courses):
        flag = 1
        for z in prerequisites:
            if z[0] == graph[k][0] and z[1] not in viz:
                flag = 0
        if flag and graph[k][0] not in viz:
            viz.add(graph[k][0])
            if search(graph, viz):
                return True
        if viz == visited:
            visited_list.append(viz)
            return True


for i in range(total_courses-1):
    prerequisites[i] = [int(x) for x in input().split()]
    verify.append(prerequisites[i][1])
    minus.append(prerequisites[i][0])

for i in minus:
    if i in verify:
        verify.remove(i)

answer = False
for i in verify:
    answer = search(prerequisites, {i})
    if answer:
        break
if answer is None:
    answer = True

print(answer)
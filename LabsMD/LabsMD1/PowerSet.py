# x = "set = [1,2,[],[1,2]]"
# x = x[7:len(x) - 1]
# card = 0
# psize = 1
# comma = 0
# pset = []
# set=[]
# for i in range(len(x)):
#     if x[i] == ',':
#         card += 1
#     if x[i]=='[':
#         bracket=i
#     if x[i]==']' and bracket<i:
#
#
# psize = pow(2, card + 1)
#
# for i in range(len(x)):
#     if x[i] == ',':
#         set.append(x[0:i])
#         comma = i
#         break
# for i in range(comma, len(x)):
#     if x[i] == ',' and comma < i:
#         set.append(x[comma + 1:i])
#         comma = i
#
# set.append(x[comma + 1:len(x)])
#
# print(set)

set=[1,2,[1],[]]
psize=pow(2,len(set))
powerset=[]
print(set)
def getnull(set):
    val = ""
    for i in range(len(set)):
        val += '0'
    return val


for i in range(psize):
    subset = []
    binvals = getnull(set)
    binvalsadd = str(bin(pow(2, len(set)) - i)).removeprefix("0b")
    binvals = binvals + binvalsadd
    binvals = list(binvals[len(binvalsadd):])
    for j in range(len(binvals)):
        if binvals[j] == '1':
            subset.append(set[j])
    powerset.append(subset)

print(powerset)

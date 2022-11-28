def getnulval(vars):
    val = ""
    for i in range(len(vars)):
        val += '0'
    return val


def makeevalstr(temp, vals, vars):
    temp = list(temp)
    for j in range(len(vars)):
        for q in range(len(temp)):
            if vars[j] == temp[q]:
                temp[q] = vals[j]
    temp = ''.join(temp)
    return temp

inputstr="(!x + y) * z + (!z * y * k)"

#DO NOT USE A,N,D,O,T,R AS VARIABLES

vars = []

for m in inputstr:
    if m.isalpha() and m not in vars:
        vars.append(m)
secstr = inputstr.replace("!", " not ").replace("+", " or ").replace("*", " and ")

print(str(vars).replace('[','|').replace(']','|').replace("'",' ').replace(',','|'), inputstr)

for i in range(1, pow(2, len(vars))):
    vals = getnulval(vars)
    valsadd = str(bin(pow(2, len(vars)) - i)).removeprefix("0b")
    vals = vals + valsadd
    vals = list(vals[len(valsadd):])
    evalstr = makeevalstr(secstr, vals, vars)
    ans = eval(evalstr)
    if ans == True or ans == "True":
        ans = 1
    elif ans == False or ans == "False":
        ans = 0
    print(str(vals).replace('[', '|').replace(']', '|').replace("'", ' ').replace(',', '|'), ans)

vals=[]
for i in range(len(vars)):
    vals.append('0')

print(str(vals).replace('[', '|').replace(']', '|').replace("'", ' ').replace(',', '|'), ans)

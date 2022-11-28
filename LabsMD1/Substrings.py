test = input()
substr = {}
for i in range(len(test) + 1):
    for j in range(len(test) + 1):
        if len(test[i:j]) > 0:
            substr.update({test[i:j]: 0})


for x in substr:
    for i in range(len(test) + 1):
        for j in range(len(test) + 1):
            if len(x) == len(test[i:j]) and x == test[i:j]:
                substr[x] += 1    
    substr[x]-=1
                
maxlen=0
ans=""
                
for x in substr:
    if len(x)>maxlen and substr[x]!=0:
        maxlen=len(x)
        ans=x

if(ans==""):
    print("''")
else:
    print(ans)
maxlen=0

#second programme

# for x in substr:
#     print(substr)

for x in substr:
    repeats=False
    for i in range(len(x)):
        for j in range(len(x)):
            if i!=j and x[i]==x[j]:
                repeats=True
    if not repeats and len(x)>maxlen:
        maxlen=len(x)
        ans=x

print(ans)
print(len(ans))

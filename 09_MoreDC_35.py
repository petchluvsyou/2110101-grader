n = int(input())
d = {}
for i in range(n):
    x = input()
    y = x.split()
    c = 0
    for i in y:
        if c==0:
            c=1
            continue
        if i not in d:
            d[i]=set()
        d[i].add(x)
ans = {}
y = input().split()
l = len(y)
for i in y:
    if i not in d:continue
    for x in d[i]:
        if x not in ans:ans[x]=1
        else:ans[x]+=1
ansans = []
for x in ans:
    if ans[x]==l:ansans.append(x)
ansans.sort()
if ansans==[]:print('Not Found')
else:
    for x in ansans:
        print(x)
r = {}
while True:
    x = input().split()
    if len(x)==1:break
    y,z = x
    if y not in r:r[y]={y}
    if z not in r:r[z]={z}
    r[y].add(z)
    r[z].add(y)
ans = set()
x = x[0]
if x not in r:r[x]={x}
for i in r[x]:
    ans.add(i)
    for j in r[i]:
        ans.add(j)
anss = []
for i in ans:
    anss.append(i)
anss.sort()
for i in anss:
    print(i)

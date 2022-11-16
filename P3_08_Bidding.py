n = int(input())
t=0
D = {}
ids = []
for i in range(n):
    t+=1
    k = input().split()
    if k[0]=='B':
        b,i,c = k[1:]
        if b not in ids: ids.append(b)
        c = int(c)
        if i not in D: D[i]={b:[c,t]}
        else:
            D[i][b]=[c,t]
    elif k[0]=='W':
        b,i = k[1:]
        if b not in ids: ids.append(b)
        if i in D:
            if b in D[i]: D[i].pop(b)
ans = []
for k in D:
    L = []
    for l in D[k]:L.append([-D[k][l][0],D[k][l][1],l])
    L.sort()
    if len(L)!=0:ans.append([L[0][2],k,-L[0][0]])
ids.sort()
ans.sort()
for x in ids:
    sum = 0
    L = []
    for b,i,c in ans:
        if x==b: sum+=c;L.append(i)
    if len(L)!=0: print(x+': $'+str(sum)+' -> '+' '.join(L))
    else: print(x+': $'+str(sum))
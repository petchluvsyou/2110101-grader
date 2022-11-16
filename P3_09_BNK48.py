L = []
D = {}
while True:
    x = input().split()
    if len(x)==1: break
    L.append(x)
if x==['1']:
    for x,y,z in L:
        z = int(z)
        if y not in D: D[y]=z
        else: D[y]+=z
    L = []
    for x in D:
        L.append([-1*D[x],x])
    L.sort()
    L = [str(e[1]) for e in L]
    print(', '.join(L[:3]))
elif x==['2']:
    check = []
    for x,y,z in L:
        if [x,y] in check: continue
        check.append([x,y])
        if y not in D: D[y]=1
        else: D[y]+=1
    L = []
    for x in D:
        L.append([-1*D[x],x])
    L.sort()
    L = [str(e[1]) for e in L]
    print(', '.join(L[:3]))
else:
    L = [[a,b,int(c)] for a,b,c in L]
    L.sort()
    L2 = []
    for i in range(1,len(L)):
        if L[i-1][:-1]==L[i][:-1]: L[i][-1]+=L[i-1][-1]
    C = []
    CC = []
    for a,b,c in L:
        if b not in CC: CC.append(b)
    L = [[-c,b,a] for a,b,c in L]
    L.sort()
    for x,y,z in L:
        if z not in C:
            C.append(z)
            if y not in D:
                D[y]=1
                CC.remove(y)
            else: D[y]+=1
    CC.sort()
    L = []
    for x in D:
        L.append([-1*D[x],x])
    for x in CC:
        L.append([0,x])
    L.sort()
    L = [str(e[1]) for e in L]
    print(', '.join(L[:3]))
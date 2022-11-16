def first_fit(L,e):
    c = 0
    for a in L:
        sum = 0
        for x in a:
            sum+=x
        if sum+e<=100:
            L[c].append(e)
            break
        c+=1
    if(c==len(L)):
        L.append([e])
    return L

def best_fit(L,e):
    c = 0
    l = []
    for a in L:
        sum = 0
        for x in a:
            sum+=x
        if sum+e<=100:
            l.append([-sum,c])
        c+=1
    l.sort()
    if len(l)==0: L.append([e])
    else: L[l[0][1]].append(e)
    return L

def partition_FF(D):
    L = []
    for x in D:first_fit(L,x)
    return L

def partition_BF(D):
    L = []
    for x in D:best_fit(L,x)
    return L

exec(input().strip())
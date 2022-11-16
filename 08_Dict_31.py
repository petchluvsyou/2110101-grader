def total(pocket):
    sum = 0
    for x in pocket:
        sum+=x*pocket[x]
    return sum

def take(pocket, money_in):
    for x in money_in:
        if x not in pocket: pocket[x]=money_in[x]
        else: pocket[x]+=money_in[x]
    return pocket

def pay(pocket, amt):
    cnt = 0
    p = {}
    l = []
    for x in pocket:
        l.append([-x,pocket[x]])
    l.sort()
    for x in l:
        v = -x[0]
        a = x[1]
        if v>amt: continue
        else:
            u = amt//v
            if u>=a:
                amt-=a*v
                p[v]=a
            else:
                amt-=u*v
                p[v]=u
    if amt==0:
        for x in p:
            pocket[x]-=p[x]
        return p
    else: return {}



exec(input().strip())
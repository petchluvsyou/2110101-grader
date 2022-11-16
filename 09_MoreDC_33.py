def add_poly(p1, p2):
    d = {}
    for x,y in p1:
        if y not in d:d[y]=x
        else:d[y]+=x
    for x,y in p2:
        if y not in d:d[y]=x
        else:d[y]+=x
    l = []
    for x in d:
        l.append([-x,d[x]])
    l.sort()
    ans = []
    for x,y in l:
        if y!=0: ans.append((y,-x))
    return ans

def mult_poly(p1, p2):
    d = {}
    for x,y in p1:
        for z,w in p2:
            if y+w not in d:d[y+w]=x*z
            else:d[y+w]+=x*z
    l = []
    for x in d:
        l.append([-x,d[x]])
    l.sort()
    ans = []
    for x,y in l:
        if y!=0: ans.append((y,-x))
    return ans


for i in range(3):
    exec(input().strip())
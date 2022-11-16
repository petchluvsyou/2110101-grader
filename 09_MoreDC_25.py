def row_number(t, e):
    cnt = 0
    ans = -1
    for x in t:
        if e in x:ans = cnt
        cnt+=1
    return ans

def flatten(t):
    k = []
    for x in t:
        for y in x:
            if y!=0: k.append(y)
    return k

def inversions(x):
    ans = 0
    for i in range(len(x)):
        for j in range(i):
            if x[j]>x[i]:ans+=1
    return ans

def solvable(t):
    inv = inversions(flatten(t))
    r = len(t)
    if inv%2==0 and r%2!=0:return True
    if inv%2==0 and r%2==0 and row_number(t,0)%2!=0:return True
    if inv%2!=0 and r%2==0 and row_number(t,0)%2==0:return True
    else: return False

exec(input().strip())
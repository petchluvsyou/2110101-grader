from re import T


def is_odd(n):
    if n%2!=0: return True
    else: return False

def has_odds(x):
    t = False
    for i in x:
        if i%2!=0: t=True
    return t

def all_odds(x):
    t= True
    for i in x:
        if i%2==0: t=False
    return t

def no_odds(x):
    t= True
    for i in x:
        if i%2!=0: t=False
    return t

def get_odds(x):
    o = []
    for i in x:
        if i%2!=0: o.append(i)
    return o

def zip_odds(a, b):
    ans = []
    a = get_odds(a)
    b = get_odds(b)
    l1 = len(a)
    l2 = len(b)
    for i in range(min(l1,l2)):
        ans.append(a[i])
        ans.append(b[i])
    for i in range(min(l1,l2),l1):
        ans.append(a[i])
    for i in range(min(l1,l2),l2):
        ans.append(b[i])
    return ans

exec(input().strip())
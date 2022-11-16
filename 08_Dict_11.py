def reverse(d):
    rev = {}
    for x in d:
        rev[d[x]]=x
    return rev
    
def keys(d, v):
    ans = []
    for x in d:
        if d[x]==v:ans.append(x)
    return ans

exec(input().strip())
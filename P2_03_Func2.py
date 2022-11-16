def convex_polygon_area(p):
    ans = 0
    p.append(p[0])
    for i in range(len(p)-1):
        ans+=p[i][0]*p[i+1][1]-p[i][1]*p[i+1][0]
    ans=abs(ans)*0.5
    return ans

def is_heterogram(s):
    ans = True
    s = s.lower()
    c = {}
    for x in s:
        if 'a'<=x<='z':
            if x not in c: c[x]=1
            else: ans = False
    return ans

def replace_ignorecase(s, a, b):
    ans=''
    l = len(a)
    i=0
    while i<len(s):
        if s[i:i+l].lower()==a.lower():
            ans+=b
            i+=l
        else:
            ans+=s[i]
            i+=1
    return ans

def top3(votes):
    l = []
    for x in votes:
        l.append([-votes[x],x])
    l.sort()
    return [l[0][1],l[1][1],l[2][1]]

for k in range(2):
    exec(input().strip())
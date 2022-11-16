inp = input().lower()
cnt = {}
for x in inp:
    if not 'a'<=x<='z':continue
    if x not in cnt:cnt[x]=1
    else:cnt[x]+=1
s = []
for x in cnt:
    s.append([-cnt[x],x])
s.sort()
for x in s:
    print(x[1]+' -> '+str(-x[0]))

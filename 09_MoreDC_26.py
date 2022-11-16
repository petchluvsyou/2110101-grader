n = int(input())
d = {}
ans = []
for i in range(n):
    x,y = input().strip().split(': ')
    y = y.split(', ')
    d[x]=[i,y]
x = input().strip()
if x not in d:print('Not Found')
else:
    for w in d:
        for q in d[x][1]:
            if w==x: continue
            if q in d[w][1]:
                if [d[w][0],w] not in ans:ans.append([d[w][0],w])
    ans.sort()
    if len(ans)!=0:
        for q in ans:print(q[1])
    else: print('Not Found')
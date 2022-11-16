n = int(input())
d = {}
for i in range(n):
    x,y = input().split()
    d[x]=int(y)
n = int(input())
l = []
for i in range(n):
    x = input().split()
    l.append([-float(x[1]),x[0],x[2:]])
l.sort()
ans = []
for i,j,k in l:
    for kk in k:
        if d[kk]!=0:
            d[kk]-=1
            ans.append([j,kk])
            break
ans.sort()
for x,y in ans:
    print(x,y)
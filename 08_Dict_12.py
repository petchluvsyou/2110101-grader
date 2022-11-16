n = int(input())
d = {}
for i in range(n):
    x,y = input().split()
    d[x]=y
    d[y]=x
n = int(input())
for i in range(n):
    x = input()
    if x in d: print(d[x])
    else: print('Not found')


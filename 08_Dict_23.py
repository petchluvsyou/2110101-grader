n = int(input())
d = {}
for i in range(n):
    x,y,z = input().split()
    x = ' '.join([x,y])
    d[x]=z
    d[z]=x
n = int(input())
for i in range(n):
    x = input()
    if x not in d: print(x+' --> Not found')
    else: print(x+' --> '+d[x])
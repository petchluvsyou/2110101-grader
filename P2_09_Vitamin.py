n = int(input())
x = input().strip().split()
f = {}
ff = {}
ff[x[0]]=[0,' '.join(x)]
f[x[0]]=' '.join(x)
v = []
for i in range(len(x)):
    v.append(list())
v[0].append(x[0])
for j in range(1,len(x)):v[j].append(float(x[j]))
for i in range(1,n):
    x = input().strip().split()
    v[0].append(x[0])
    ff[x[0]]=[i+1,' '.join(x)]
    f[x[0]]=' '.join(x)
    for j in range(1,len(x)):v[j].append(float(x[j]))
o = input().strip().split()
if o[0]=='show':
    ll = []
    for x in ff:ll.append([ff[x][0],ff[x][1]])
    ll.sort()
    for x in ll:
        print(x[1])
elif o[0]=='get':
    if o[1] in f:print(f[o[1]])
    else:print(o[1]+' not found')
elif o[0]=='avg':
    sum=0
    for x in v[int(o[1])]:sum+=x
    print(round(sum/n,4))
elif o[0]=='max':
    o[1]=int(o[1])
    l = []
    for i in range(len(v[o[1]])):
        l.append([-v[o[1]][i],v[0][i]])
    l.sort()
    print(l[0][1],-l[0][0])
elif o[0]=='min':
    o[1]=int(o[1])
    l = []
    for i in range(len(v[o[1]])):
        l.append([v[o[1]][i],v[0][i]])
    l.sort()
    print(l[0][1],l[0][0])
elif o[0]=='sort':
    o[1]=int(o[1])
    l = []
    for i in range(len(v[o[1]])):
        l.append([v[o[1]][i],v[0][i]])
    l.sort()
    for a,b in l:
        print(b,end=' ')
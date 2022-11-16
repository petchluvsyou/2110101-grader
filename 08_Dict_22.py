n = int(input())
ic = {}
for i in range(n):
    x,y = input().split()
    ic[x]=float(y)
sales = {}
n = int(input())
for i in range(n):
    x,y = input().split()
    y = float(y)
    if (x not in sales) and (x in ic):sales[x]=ic[x]*y
    elif x in ic:sales[x]+=ic[x]*y
sum = 0
l = []
for x in sales:
    sum+=sales[x]
    l.append([-sales[x],x])
l.sort()
if sum==0: print('No ice cream sales')
else:
    topsale = -l[0][0]
    print('Total ice cream sales:',str(sum))
    ll = []
    for x in sales:
        if sales[x]==topsale:ll.append(x)
    ll.sort()
    print('Top sales:',end=' ')
    for i in range(len(ll)-1):print(ll[i],end=', ')
    print(ll[len(ll)-1])
 
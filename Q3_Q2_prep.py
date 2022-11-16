n = int(input())
ids = {}
for i in range(n):
    name,id,m = input().split()
    m = float(m)
    ids[id]=[name,m]
while True:
    inp = input()
    if inp=='exit': break
    l = inp.split()
    if l[2]=='transfer':
        name1,id1,x,id2,m = l
        m = float(m)
        if id1 not in ids or ids[id1][0]!=name1 or id2 not in ids:
            print('Transaction Failed')
            continue
        ids[id2][1]+=m
        ids[id1][1]-=m
        if int(ids[id2][1])==ids[id2][1]: ids[id2][1]=int(ids[id2][1])
        if int(ids[id1][1])==ids[id1][1]: ids[id1][1]=int(ids[id1][1])
        print(ids[id1][0]+' ('+id1+') '+str(ids[id1][1]))
        print(ids[id2][0]+' ('+id2+') '+str(ids[id2][1]))
    elif l[2]=='deposit':
        name1,id1,x,m = l
        m = float(m)
        if id1 not in ids: ids[id1]=[name1,0]
        if ids[id1][0]!=name1:
            print('Transaction Failed')
            continue
        ids[id1][1]+=m
        if int(ids[id1][1])==ids[id1][1]: ids[id1][1]=int(ids[id1][1])
        print(ids[id1][0]+' ('+id1+') '+str(ids[id1][1]))
    else:
        name1,id1,x,m = l
        m = float(m)
        if id1 not in ids: ids[id1]=[name1,0]
        if ids[id1][0]!=name1 or m>ids[id1][1]:
            print('Transaction Failed')
            continue
        ids[id1][1]-=m
        if int(ids[id1][1])==ids[id1][1]: ids[id1][1]=int(ids[id1][1])
        print(ids[id1][0]+' ('+id1+') '+str(ids[id1][1]))
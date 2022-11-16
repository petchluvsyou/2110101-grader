a = input()
b = input()
aa = {}
bb = {}
for x in a.lower():
    if not 'a'<=x<='z':continue
    if x not in aa:aa[x]=1
    else:aa[x]+=1
for x in b.lower():
    if not 'a'<=x<='z':continue
    if x not in bb:bb[x]=1
    else:bb[x]+=1
c={}
for x in aa:
    if x not in c:c[x]=aa[x]
    else:c[x]=min(c[x],aa[x])
for x in bb:
    if x not in c:c[x]=bb[x]
    else:c[x]=min(c[x],bb[x])
l = []
print(a)
for x in aa:
    if x not in bb:l.append([x,aa[x]])
    if aa[x]>c[x]:l.append([x,aa[x]-c[x]])
l.sort()
if len(l)==0:
    print('- None')
else:
    for x,y in l:
        print('- remove '+str(y)+' '+x,end='')
        if y>1:print('\'s',end='')
        print()
l = []
print(b)
for x in bb:
    if x not in aa:l.append([x,bb[x]])
    if bb[x]>c[x]:l.append([x,bb[x]-c[x]])
l.sort()
if len(l)==0:
    print('- None')
else:
    for x,y in l:
        print('- remove '+str(y)+' '+x,end='')
        if y>1:print('\'s',end='')
        print()
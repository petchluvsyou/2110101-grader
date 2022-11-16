fil = input()
c = input()
f = open(fil,'r')
dot = []
text = []
for l in f:
    l = l.strip()
    text.append(l)
    if dot==[]:dot=[1]*len(l)
    for i in range(len(l)):
        if l[i]!='.':dot[i]=0
if c=='LSTRIP':
    s = 0
    while dot[s]==1:s+=1
    for l in text:
        print(l[s:]) 
elif c=='RSTRIP':
    s = len(dot)-1
    while dot[s]==1:s-=1
    for l in text:
        print(l[:s+1])
elif c=='STRIP':
    s = 0
    while dot[s]==1:s+=1
    e = len(dot)-1
    while dot[e]==1:e-=1
    for l in text:
        print(l[s:e+1])
elif c=='STRIP_ALL':
    for l in text:
        for i in range(len(dot)):
            if dot[i]==0: print(l[i],end='')
        print()
else: print('Invalid command')
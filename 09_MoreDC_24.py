l = []
d = {}
c = 0
while True:
    x = input()
    if x=='q':break
    a,b = x.split(', ')
    h = 0
    for x in l:
        if x[0]==b:h = 1
    if h==0: l.append([b])
    for x in l:
        if x[0]==b:x.append(a)
for x in l:
    print(x[0]+': ',end='')
    c=0
    for y in x:
        if c==0:c=1
        elif c==1:
            print(y,end='')
            c=2
        else:print(', '+y,end='')
    print()


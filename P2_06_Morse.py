inp = input()
f = open(inp,'r')
cnt = 0
d = {}
for l in f:
    if cnt==0:o=l.strip()
    elif cnt==1:
        v = l.strip().split('[')
        for x in v:
            if x=='':continue
            d[x[0]]=x[2:]
            d[x[2:]]=x[0]
    elif o=='T2M':
        p=1
        for x in l.strip():
            if x not in d:
                p=0
        if p:
            for x in l.strip():
                print(d[x],end=' ')
        else:print('Invalid : '+l.strip(),end='')
        print()
    elif o=='M2T':
        p=1
        for x in l.strip().split():
            if x not in d:
                p=0
        if p:
            for x in l.strip().split():
                print(d[x],end='')
        else:print('Invalid : '+l.strip(),end='')
        print()
    else: print('Invalid code')
    cnt+=1

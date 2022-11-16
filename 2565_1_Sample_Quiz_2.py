fi = input()
txt = input()
rep = input()
txts = txt.lower()+'/'
rep = rep+'/'

f = open(fi,'r')
for ll in f:
    L = []
    l = ll.lower()
    for i in range(len(l)-len(txts)+1):
        if i!=0:
            if l[i-1]!='/': continue
        p = 1
        for k in range(len(txts)):
            if txts[k]=='?':continue
            else:
                if txts[k]!=l[k+i]:
                    p=0
                    break
        if p==1: L.append(i)
    ll = list(ll)
    x = len(rep)-len(txts)
    cnt = 0
    for i in L:
        i = int(i)
        ll[i+x*cnt:i+x*cnt+len(txts)] = rep
        cnt+=1
    for x in ll: print(x,end='')
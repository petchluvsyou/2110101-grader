N = int(input())
sum = 0
detail = {}
for i in range(N):
    inp = input()
    l = inp.split()
    if l[0]=='Play':
        a,b,c,d = inp.split(' | ')
        c = int(c); d = int(d)
        r = int(25*(1+c)*d/(10**7))
        if b in detail:
            if r>detail[b][2]:
                sum=sum-detail[b][2]+r
                detail[b]=[c,d,r]
        else:
            detail[b]=[c,d,r]
            sum+=r
    elif l[0]=='Rating' and len(l)==1:
        print(sum)
    elif l[0]=='Rating':
        a,b = inp.split(' | ')
        if b in detail: print(detail[b][2])
        else: print(0)
    else:
        a,b = inp.split(' | ')
        if b not in detail: print(b+': No play history')
        else: print(' | '.join([b,str(detail[b][0]),str(detail[b][1]),str(detail[b][2])]))
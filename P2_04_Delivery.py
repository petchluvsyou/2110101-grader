mm=[31,28,31,30,31,30,31,31,30,31,30,31]
mm2=[31,29,31,30,31,30,31,31,30,31,30,31]
dtype={'E':1,'Q':3,'N':7,'F':14}
l = []
while True:
    inp = input()
    if inp=='END':break
    n,o,d,m,y = inp.split()
    d=int(d)
    m=int(m)
    y=int(y)
    if y<2558:
        print('Error: '+inp+' --> Invalid year')
        continue
    if not 1<=m<=12:
        print('Error: '+inp+' --> Invalid month')
        continue
    if ((y-543)%4==0 and (y-543)%100!=0) or (y-543)%400==0:
        if d>mm2[m-1] or d<=0:
            print('Error: '+inp+' --> Invalid date')
            continue
    else:
        if d>mm[m-1] or d<=0:
            print('Error: '+inp+' --> Invalid date')
            continue
    if o not in ['E','Q','N','F']:
        print('Error: '+inp+' --> Invalid delivery type')
        continue
    days = d
    if ((y-543)%4==0 and (y-543)%100!=0) or (y-543)%400==0:
        i=0
        while m>i+1:
            days+=mm2[i]
            i+=1
        days+=dtype[o]
        i=0
        m=1
        if days>366:
            days-=366
            y+=1
        while i<12 and days>mm2[i]:
            m+=1
            days-=mm2[i]
            i+=1
        d=days
    else:
        i=0
        while m>i+1:
            days+=mm[i]
            i+=1
        days+=dtype[o]
        i=0
        m=1
        if days>365:
            days-=365
            y+=1
        while i<12 and days>mm[i]:
            m+=1
            days-=mm[i]
            i+=1
        d=days
    l.append([y,m,d,n])
l.sort()
for y,m,d,n in l:
    print(n+': delivered on '+str(d)+'/'+str(m)+'/'+str(y))


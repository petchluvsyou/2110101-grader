n = int(input())
d = {}
for i in range(n):
    x = input().strip().split(', ')
    g = x[-2]
    t = x[-1].split(':')
    s = int(t[0])*60+int(t[1])
    if g not in d:d[g]=s
    else:d[g]+=s
l = []
for x in d:
    l.append([-d[x],x])
l.sort()
if len(l)<=3:
    for x,y in l:
        x = -x
        if x%60>=10:print(y+' --> '+str(x//60)+':'+str(x%60))
        else:print(y+' --> '+str(x//60)+':0'+str(x%60))
else:
    c = 0
    for x,y in l:
        if c==3:break
        x = -x
        if x%60>=10:print(y+' --> '+str(x//60)+':'+str(x%60))
        else:print(y+' --> '+str(x//60)+':0'+str(x%60))
        c+=1

'''
9
Shake It Off, Taylor Swift, Pop, 3:39
Rolling In The Deep, Adele, Pop, 3:48
Chandelier, Sia, Pop, 3:36
Roar, Katy Perry, Pop, 3:42
Hotel California, Eagle, Rock, 6:30
We Are the Champions, Queen, Rock, 2:59
Hello Dolly, Louis Armstrong, Jazz, 2:27
Bohemian Rhapsody, Queen, Rock, 5:55
Coward of the County, Kenny Rogers, Country, 4:02
'''
n1, m1, d1, y1 = [e for e in input().split()]
n2, m2, d2, y2 = [e for e in input().split()]
mmm = {'January':'01',
     'February':'02',
     'March':'03',
     'April':'04',
     'May':'05',
     'June':'06',
     'July':'07',
     'August':'08',
     'September':'09',
     'October':'10',
     'November':'11',
     'December':'12'}
m1 = mmm[m1]
m2 = mmm[m2]
d1 = d1[0:len(d1)-1]
d2 = d2[0:len(d2)-1]
if len(d1)==1:
    d1 = '0'+d1
if len(d2)==1:
    d2 = '0'+d2
b1 = int(y1+m1+d1)
b2 = int(y2+m2+d2)
if b1<b2:
    print(n1)
elif b1>b2:
    print(n2)
else:
    print(n1,n2)
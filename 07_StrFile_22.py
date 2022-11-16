inp1 = input().lower()
inp2 = input().lower()
c = 'abcdefghijklmnopqrstuvwxyz0123456789'
i1 = [0]*36
i2 = [0]*36
for x in inp1:
    k = c.find(x)
    if k!=-1:i1[k]+=1
for x in inp2:
    k = c.find(x)
    if k!=-1:i2[k]+=1  
if i1==i2:print('YES')
else:print('NO')
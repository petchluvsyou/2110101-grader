d,m,y = [int(e) for e in input().split()]
month = [31,28,31,30,31,30,31,31,30,31,30,31]
sum = d+15
m = m-1
while m!=0:
    m = m-1
    sum = sum+month[m]
    if m==1 and ((y%4==3 and (y-543)%100!=0) or (y-543)%400==0):
        sum = sum+1
if sum>366 and ((y%4==3 and (y-543)%100!=0) or (y-543)%400==0):
    y = y+1
    sum = sum-366
elif sum>365 and y%4!=3:
    y = y+1
    sum = sum-365
while sum>month[m]:
    sum = sum-month[m]
    m = m+1
    if m==1 and sum!=1 and ((y%4==3 and (y-543)%100!=0) or (y-543)%400==0):
        sum = sum-1
d = sum

print(str(d)+"/"+str(m+1)+'/'+str(y))


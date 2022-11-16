import math

def day_of_year(d, m, y):
    month = [31,28,31,30,31,30,31,31,30,31,30,31]
    sum = d
    m = m-1
    while m!=0:
        m = m-1
        sum = sum+month[m]
        if m==1 and ((y%4==3 and (y-543)%100!=0) or (y-543)%400==0):
            sum = sum+1
    return sum

bd,bm,by,d,m,y = [int(e) for e in input().split()]
sumb = day_of_year(bd,bm,by)
sum = day_of_year(d,m,y)
if (by%4==3 and (by-543)%100!=0) or (by-543)%400==0:
    sumb = 366-sumb
else:
    sumb = 365-sumb
b = 365*(y-by-1)
t = sumb+b+sum
print(t,"{:.2f}".format(math.sin(2*math.pi*t/23)),"{:.2f}".format(math.sin(2*math.pi*t/28)),"{:.2f}".format(math.sin(2*math.pi*t/33)))
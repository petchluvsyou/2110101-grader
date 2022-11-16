import math

a,b,c = input().split(",")
b = '0'+b
f = len(b)-1
g = len(c)
a = int(a)
b = int(b)
c = int(c)
d = 10**g-1
x = (a*10**f+b)*d+c
y = d*10**f
gcd = math.gcd(x,y)
x = x//gcd
y = y//gcd
print(str(x)+" / "+str(y))
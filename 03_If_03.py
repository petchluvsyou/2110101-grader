a,b,c,d = [float(i) for i in input().split()]
sum = a+b+c+d
ma = a
mi = a
if ma<b:
    ma=b
if mi>b:
    mi=b
if ma<c:
    ma=c
if mi>c:
    mi=c
if ma<d:
    ma=d
if mi>d:
    mi=d
sum = (sum-mi-ma)/2
print(round(sum,2))

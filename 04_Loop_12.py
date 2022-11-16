n = int(input())
x = []
y = []

for i in range(n):
    xi, yi = [int(e) for e in input().split()]
    x.append(xi)
    y.append(yi)
c = input()
mi = 2e9
ma = -2e9
if c[1]=='i':
    for i in range(n):
        if(i%2==0):
            mi=min(x[i],mi)
            ma=max(y[i],ma)
        else:
            mi=min(y[i],mi)
            ma=max(x[i],ma)
else:
    for i in range(n):
        if(i%2!=0):
            mi=min(x[i],mi)
            ma=max(y[i],ma)
        else:
            mi=min(y[i],mi)
            ma=max(x[i],ma)
print(mi,ma)

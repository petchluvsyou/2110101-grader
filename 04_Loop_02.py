a = float(input())
L = 0
U = a
x = (L+U)/2
while not (abs(a-10**x)<=10**-10*max(a,x**2)):
    if 10**x>a:
        U = x
    else:
        L = x
    x = (L+U)/2
print(round(x,6))
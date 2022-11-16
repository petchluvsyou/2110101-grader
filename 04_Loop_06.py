a = float(input())
L = 0
aa = a
U = 0
while aa!=0:
    aa = aa//10
    U += 1
b = (L+U)/2
while not abs(a-10**b)<=10**-10*max(a,10**b):
    if 10**b>a:
        U=b
    else:
        L=b
    b = (L+U)/2
print(round(b,6))
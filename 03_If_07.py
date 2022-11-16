x = input()
l = len(x)
x = int(x)
if l<=3:
    print(x)
elif l==4:
    print(round(x/10**3,1),end='')
    print("K")
elif l==5 or l==6:
    print(round(x/10**3),end='')
    print("K")
elif l==7:
    print(round(x/10**6,1),end='')
    print("M")
elif l==8 or l==9:
    print(round(x/10**6),end='')
    print("M")
elif l==10:
    print(round(x/10**9,1),end='')
    print("B")
else:
    print(round(x/10**9),end='')
    print("B")
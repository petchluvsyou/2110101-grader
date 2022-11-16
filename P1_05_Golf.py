p = 0
s = 0
sa = 0
for i in range(9):
    x,y,z = [int(f) for f in input().split()]
    p = p+x
    s = s+y
    if z:
        sa += min(x+2,y)
sa = int((0.8*(1.5*sa-p))//1)
print(s)
print(sa)
print(s-sa)


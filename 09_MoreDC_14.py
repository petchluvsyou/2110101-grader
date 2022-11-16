a = input()
b = input()
c = input()
C = {}
T = {}
l = []
f = open(a,'r')
for line in f:
    k1,k2 = line.strip().split(',')
    C[k1]=k2
f.close()
f = open(b,'r')
for line in f:
    k1,k2 = line.strip().split(',')
    T[k1]=k2
f.close()
f = open(c,'r')
for line in f:
    k1,k2 = line.strip().split(',')
    if k1 in C and k2 in T:print(C[k1]+','+T[k2])
    else:print('record error')
f.close()

f = open('00_intro_03.py','r')
L = []
for i in f:
    L.append(i)
L = L[::-1]
for i in L:
    print(i[::-1])
f.close()
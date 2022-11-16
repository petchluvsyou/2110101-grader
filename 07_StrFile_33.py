inp1,inp2 = input().strip().split()
s = []
f = open(inp1,'r')
for l in f:
    l = l.strip()
    id = l
    fa = id[8:10]
    s.append([fa,id])
f.close()
f = open(inp2,'r')
for l in f:
    l = l.strip()
    id = l
    fa = id[8:10]
    s.append([fa,id])
f.close()
s.sort()
for x in s:print(x[1])
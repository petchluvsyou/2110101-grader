n = int(input())
d = {}
for i in range(n):
    l = []
    x = input().split()
    for j in x:
        if j not in l:l.append(j)
    for j in l:
        if j not in d:d[j]=1
        else:d[j]+=1
print(len(d))
c = 0
for i in d:
    if d[i]==n:c+=1
print(c)
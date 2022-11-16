n = int(input())
d = {}
for i in range(n):
    w,l = input().split()
    if w not in d: d[w]=1
    if l not in d: d[l]=0
    if l in d: d[l]=0
W = []
for x in d:
    if d[x]==1:W.append(x)
print(W)
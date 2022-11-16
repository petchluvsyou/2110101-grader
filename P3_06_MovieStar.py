N = int(input())
mov = []
for x in range(N):
    mov.append([e.strip() for e in input().split(',')])
act = [e.strip() for e in input().split(',')]
for x in act:
    L = []
    for y in mov:
        if x in y[1:]: L.append(y[0])
    if len(L)!=0: print(x+' -> '+', '.join(L))
    else: print(x+' -> Not found')
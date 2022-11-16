N = int(input())
L = []
for x in range(N):
    name = input()
    L.append([name,input().split()])
while True:
    x = input()
    if x=='-1': break
    S = []
    repeat = []
    for name,a in L:
        cnt = 0
        for b in a:
            if b not in repeat: repeat.append(b)
            if b==x: cnt+=1
        S.append([-cnt/len(a)/len(repeat),name])
    S.sort()
    if S[0][0]!=0: print(S[0][1])
    else: print('NOT FOUND')
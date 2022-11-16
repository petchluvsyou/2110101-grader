L = []
votesum = {}
n = int(input())
for i in range(n):
    x = input()
    L.append(x)
    votesum[x]=[0,0,0]
n = int(input())
D = {}
DD = {}
for i in range(n):
    x,y = input().split()
    D[x]=y
    if y not in DD: DD[y]=[x]
    else: DD[y].append(x)
n = int(input())
vote = {}
for i in range(n):
    x,y = input().split()
    if y=='Y':
        votesum[D[x]][0]+=1
        vote[x]=0
    elif y=='N':
        votesum[D[x]][1]+=1
        vote[x]=1
    else:
        votesum[D[x]][2]+=1
        vote[x]=2
for x in L:
    print(x)
    ans = []
    m = max(votesum[x])
    i = -1
    for y in votesum[x]:
        if y==m:i+=1
    if i:
        print('Inconclusive')
        continue
    for y in DD[x]:
        if y not in vote: continue
        if votesum[x][vote[y]]!=m: ans.append(y)
    ans.sort()
    if ans==[]: print('No cobra')
    else: print(', '.join(ans))

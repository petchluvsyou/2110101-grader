fi = input()
n = int(input())
for i in range(n//10): print('-'*9+str(i+1),end='')
print('-'*(n-10*(n//10)),end='')
print()
L = []
f = open(fi,'r')
for l in f:
    L.append(l.strip())
f.close()
L = '.'.join(L)
w = ''
dot = 0
W = []
for x in L:
    if x=='.':
        if w!='':
            W.append([w,dot])
            dot=0;w=''
        dot+=1
    else: w+=x
W.append([w,dot])
s = 0
for x,y in W:
    if len(x)+y+s<=n:
        print('.'*y+x,end='')
        s+=len(x)+y
    else:
        print('\n'+x,end='')
        s=len(x)


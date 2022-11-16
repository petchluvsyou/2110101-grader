n = int(input())
k = int(input())

if (n<1 or n>15) and (k<1 or k>100): print('Invalid n and k')
elif n<1 or n>15: print('Invalid n')
elif k<1 or k>100: print('Invalid k')
else:
    for i in range(1,k+1):
        if i!=k: print(str(i)+'-'*(n-len(str(i))+1),end='')
        else: print(str(i)+'-'*(n-len(str(i))),end='')
    print()
    L = ['0','1']
    for j in range(n-1):
        for i in range(len(L)-1,-1,-1): L.append(L[i]) 
        for i in range(2**(j+1)): L[i]='0'+L[i]
        for i in range(2**(j+1),2**(j+2)): L[i]='1'+L[i]
    i=0
    while i<len(L):
        print(','.join(L[i:i+k]))
        i+=k

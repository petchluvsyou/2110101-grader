x = input().split()
k = int(input())
re = 1
sum=0
sumall=int(x[0])
for i in range(1,len(x)):
    sumall+=int(x[i])
    if x[i]==x[i-1]: re+=1
    else:
        if re>=k:sum+=re*int(x[i-1])
        re=1
if re>=k:sum+=re*int(x[len(x)-1])
print(sumall-sum)


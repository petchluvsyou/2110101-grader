ans = []
a = 0
n = int(input())
for i in range(n):
    a+=1
    x = int(input())
    if a%2==0:
        ans = [x]+ans
    else:
        ans = ans+[x]
n = input().split()
for x in n:
    x = int(x)
    a+=1
    if a%2==0:
        ans = [x]+ans
    else:
        ans = ans+[x]
x = 0
while True:
    a+=1
    x = int(input())
    if x==-1:
        break
    if a%2==0:
        ans = [x]+ans
    else:
        ans = ans+[x]
print(ans)

n = int(input())
for i in range(n):
    x = input()
    cnt=0
    for y in x:
        if y!='.':break
        cnt+=1
    print('.'*(cnt//2)+x[cnt:])
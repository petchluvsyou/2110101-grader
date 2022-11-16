inp = input()+'0000'
l = []
spare = []
for i in inp:
    if i=='X':
        l.append(10)
        spare.append(0)
    elif i=='/':
        l.append(10-l[len(l)-1])
        spare.append(1)
    else:
        l.append(int(i))
        spare.append(0)
score = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
cnt = -1
for i in range(len(l)):
    cnt += 1
    if l[i]==10:
        score[cnt//2]+=l[i]+l[i+1]+l[i+2]
        cnt+=1
    else:
        if spare[i]==1:
            score[cnt//2]+=l[i]+l[i+1]
        else:
            score[cnt//2]+=l[i]
sum = 0
for i in range(10):
    sum += score[i]
x = int(input())
if x<11 and x>0:
    print(score[x-1])
else:
    print(sum)



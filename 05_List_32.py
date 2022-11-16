q = []
idx = -1
nn = 0
sum = 0
n = int(input())
for k in range(n):
    c = input().split()
    if c[0]=='reset':
        x = int(c[1])
    elif c[0]=='new':
        print('ticket',str(x))
        q.append([x,int(c[1])])
        x=x+1
    elif c[0]=='next':
        idx+=1
        print('call',str(q[idx][0]))
    elif c[0]=='order':
        sum+=(int(c[1])-q[idx][1])
        nn+=1
        print('qtime',str(q[idx][0]),str(int(c[1])-q[idx][1]))
    elif c[0]=='avg_qtime':
        avg = round(sum/nn,4)
        print('avg_qtime',str(round(avg,4)))

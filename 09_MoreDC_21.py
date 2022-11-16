def factor(N):
    y=N
    prime = []
    d = []
    i = 2
    while(i*i<=N):
        p=1
        for x in prime:
            if x*x>i:break
            if i%x==0:
                p=0
                break
        if p:
            prime.append(i)
            cnt=0
            while y%i==0:
                y//=i
                cnt+=1
            if cnt:d.append([i,cnt])
        i+=1
    if y!=1:d.append([y,1])
    return d

exec(input().strip())

#print(factor(13*17))
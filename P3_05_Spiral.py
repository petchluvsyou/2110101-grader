def spiral_square(n):
    S = []
    for i in range(n):
        S.append([0]*n)
    val = n**2
    posx,posy = n-1,n
    di = 'w'
    cnt = 0
    lim = n*2
    while val!=0:
        cnt+=1
        if di=='w':
            posy-=1
            if cnt==lim//2:di='n';cnt=0;lim-=1
        elif di=='n':
            posx-=1
            if cnt==lim//2: di='e';cnt=0;lim-=1
        elif di=='e':
            posy+=1
            if cnt==lim//2: di='s';cnt=0;lim-=1
        elif di=='s':
            posx+=1
            if cnt==lim//2: di='w';cnt=0;lim-=1
        S[posx][posy]=val
        val-=1
    return S

def print_square(S):
    for i in range(len(S)):
        print(' '.join([(2*' '+str(e))[-3:] for e in S[i]]))

exec(input().strip())
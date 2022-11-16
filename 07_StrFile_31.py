dna = input().strip().upper()
op = input().strip()
valid = ['A','T','G','C']
iv = 0
for x in dna:
    if x not in valid:
        iv = 1
if iv:print('Invalid DNA')
elif op=='R':
    rev = ''
    for x in dna:
        if x=='A':rev+='T'
        elif x=='C':rev+='G'
        elif x=='T':rev+='A'
        elif x=='G':rev+='C'
    print(rev[::-1])
elif op=='F':
    cnt = [0]*4
    for x in dna:
        u = valid.index(x)
        cnt[u]+=1
    print('A='+str(cnt[0])+', T='+str(cnt[1])+', G='+str(cnt[2])+', C='+str(cnt[3]))
elif op=='D':
    cnt=0
    xx = input().strip()
    for i in range(len(dna)-1):
        if(dna[i:i+2]==xx):cnt+=1
    print(cnt)

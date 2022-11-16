red = 6
s1 = 0
s2 = 0
score = {'R':1,'Y':2,'G':3,'W':4,'B':5,'P':6,'K':7,'X':0}
while red>0:
    inp=input()
    if inp[1]=='X': continue
    if inp[0]=='1':s1+=score[inp[1]]+score[inp[2]]
    else: s2+=score[inp[1]]+score[inp[2]]
    for x in inp:
        if x=='R':red-=1
color = 6
while color>0:
    inp=input()
    if inp[0]=='1':s1+=score[inp[1]]
    else: s2+=score[inp[1]]
    for x in inp:
        if 'RYGWBPK'.find(x)!=-1:color-=1
print(s1,s2)
if s1>s2: print('Player 1 wins')
elif s1<s2: print('Player 2 wins')
else: print('Tie')


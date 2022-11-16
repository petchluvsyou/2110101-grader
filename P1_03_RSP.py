m = int(input())
s1 = 0
s2 = 0
g = 0
while g<3*m and s1!=m and s2!=m:
    g+=1
    a,b = [e for e in input().split()] 
    if (a=='R' and b=='S') or (a=='P' and b=='R') or (a=='S' and b=='P'):
        s1 += 1
    elif a==b:
        continue
    else:
        s2 += 1
print(s1,s2)
if s1<s2:
    print('Player 2 wins')
elif s1>s2:
    print('Player 1 wins')
else:
    print('Tie')
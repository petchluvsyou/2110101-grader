def walk(x,y,step,ans):
    if step==len(word)-1:
        ans.append((x,y))
        print(ans)
        return True
    if x!=0 and table[x-1][y]==word[step+1]:
        ans.append((x,y))
        walk(x-1,y,step+1,ans)
        ans = ans[:-1]
    if x!=a-1 and table[x+1][y]==word[step+1]:
        ans.append((x,y))
        walk(x+1,y,step+1,ans)
        ans = ans[:-1]
    if y!=0 and table[x][y-1]==word[step+1]:
        ans.append((x,y))
        walk(x,y-1,step+1,ans)
        ans = ans[:-1]
    if y!=b-1 and table[x][y+1]==word[step+1]:
        ans.append((x,y))
        walk(x,y+1,step+1,ans)
        ans = ans[:-1]
    return False
a,b = input().split()
a,b = int(a),int(b)
table = []
for i in range(a):
    x = input()
    table.append(x)
word = input()
p=0
for i in range(a):
    if p==1: break
    for j in range(b):
        if p==1: break
        if table[i][j]==word[0]:
            if walk(i,j,0,[]): p=1
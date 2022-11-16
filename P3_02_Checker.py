inp = input().strip()
position = inp.split()
r = 1;c = 1
if len(position)<3:
    if not 1<=len(position)<=2:
        r=0;c=0
    elif len(position)==1:
        if len(inp)<2: c=0;row=inp
        else:row, col = position[0][0], position[0][1:]
    else: row, col = position[0],position[1]
else:
    i = inp.find('=')
    j = inp.find(',')
    k = inp.find('=',i+1)
    row = inp[i+1:j]
    col = inp[k+1:]
    if inp[:3]=='col': row,col = col,row
    if(len(row.split()))!=1:r=0
    else:row = row.split()[0]
    if len(row)!=1: r=0
    if(len(col.split()))!=1:c=0
    else:col = col.split()[0]
if c!=0:
    p=1
    for x in col:
        if not '0'<=x<='9': p=0
    if p==0: c=0
if c!=0:
    col=int(col)
    if not 52>=col>=1: c=0
if r!=0 and row not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz': r=0
if r==0 and c==0: print('Invalid row and column')
elif r==0: print('Invalid row')
elif c==0: print('Invalid column')
else:
    r = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'.find(row)
    if r%2 == int(col)%2 :
        print('Black')
    else:
        print('White')
inp = input()
n = '67890123456789012'
c = 'wxyzabcdefghijklmnopqrstuvwxyzabc'
p = 1
if len(inp)<8:
    p = 0
    print('Less than 8 characters')
if inp.upper()==inp:
    p = 0
    print('No lowercase letters')
if inp.lower()==inp:
    p = 0
    print('No uppercase letters')
inp=inp.lower()
cnt=0
cnt2=0
for x in inp:
    u = n.find(x)
    if u!=-1:cnt+=1
    elif c.find(x)==-1:cnt2=1
if cnt==0:
    p = 0   
    print('No numbers')
if cnt2==0:
    p = 0
    print('No symbols')
r4=0
n4=0
c4=0
for i in range(len(inp)-3):
    if inp[i]*4==inp[i:i+4]:r4=1
for i in range(len(inp)-3):
    if n.find(inp[i])!=-1:
        k = n.find(inp[i])
        if k<4:k+=10
        if inp[i:i+4]==n[k:k+4] or inp[i:i+4]==n[k:k-4:-1]:n4=1
for i in range(len(inp)-3):
    if c.find(inp[i])!=-1:
        k = c.find(inp[i])
        if k<4:k+=26
        if inp[i:i+4]==c[k:k+4] or inp[i:i+4]==c[k:k-4:-1]:c4=1
if r4:
    p = 0
    print('Character repetition')
if n4:
    p = 0
    print('Number sequence')
if c4:
    p = 0
    print('Letter sequence')
row1 = '()_+!@#$%^&*()_+!@#'
row2 = 'uiopqwertyuiopqwe'
row3 = 'hjklasdfghjklasd'
row4 = 'vbnmzxcvbnmzxc'
k4=0
for i in range(len(inp)-3):
    if row1.find(inp[i])!=-1:
        k = row1.find(inp[i])
        if k<4:k+=12
        if inp[i:i+4]==row1[k:k+4] or inp[i:i+4]==row1[k:k-4:-1]:k4=1
    if row2.find(inp[i])!=-1:
        k = row2.find(inp[i])
        if k<4:k+=10
        if inp[i:i+4]==row2[k:k+4] or inp[i:i+4]==row2[k:k-4:-1]:k4=1
    if row3.find(inp[i])!=-1:
        k = row3.find(inp[i])
        if k<4:k+=9
        if inp[i:i+4]==row3[k:k+4] or inp[i:i+4]==row3[k:k-4:-1]:k4=1
    if row4.find(inp[i])!=-1:
        k = row4.find(inp[i])
        if k<4:k+=7
        if inp[i:i+4]==row4[k:k+4] or inp[i:i+4]==row4[k:k-4:-1]:k4=1
if k4:
    p = 0
    print('Keyboard pattern')
if p:
    print('OK')


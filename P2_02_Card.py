v = {
    'A':1,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    'T':10,
    'J':11,
    'Q':12,
    'K':13
}
c = {
    'C':1,
    'D':2,
    'H':3,
    'S':4
}
inp = input()
for i in range(0,len(inp)-3,2):
    x1=v[inp[i]]
    x2=c[inp[i+1]]
    y1=v[inp[i+2]]
    y2=c[inp[i+3]]
    if x1==y1:
        if x2>y2:print('+',end='')
        print(x2-y2,end='')
    else:
        if x1>y1:print('+',end='') 
        print(x1-y1,end='')

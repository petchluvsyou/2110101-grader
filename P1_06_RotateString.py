cmd = input()
n = int(input())
invalid = 0
table = []
for i in range(n):
    x = input().strip()
    table.append(x)
    if i!=0 and len(table[i])!=len(table[i-1]):
        invalid = 1
l = len(table[0])
if invalid:
    print('Invalid size')
else:
    if cmd=='90':
        for i in range(l):
            for j in range(n):
                print(table[n-j-1][i],end='')
            print()
    elif cmd=='flip':
        for i in range(n):
            for j in range(l):
                print(table[i][l-j-1],end='')
            print()
    else:
        for i in range(n):
            for j in range(l):
                print(table[n-i-1][l-j-1],end='')
            print()
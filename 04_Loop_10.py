x = int(input())
for i in range(1,x+1):
    for j in range(x-i):
        print(' ',end='')
    print('*',end='')
    if i!=1 and i!=x:
        for k in range(2*(i-1)-1):
            print(' ',end='')
        print('*',end='')
    elif i==x:
        for k in range(2*(i-1)-1):
            print('*',end='')
        print('*',end='')
    print('\n')
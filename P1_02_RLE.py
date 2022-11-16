cmd = input()
if cmd == 'str2RLE':
    z = input()
    z = z+''
    pv = '#'
    cnt = 0
    for i in z:
        if i!=pv:
            if pv!='#':
                print(pv,cnt,end = ' ')
            cnt = 1
            pv = i
        else:
            cnt = cnt+1
    print(pv,cnt)
elif cmd == 'RLE2str':
    x = input().split()
    for i in range(len(x)//2):
        for j in range(int(x[2*i+1])):
            print(x[2*i],end='')
else:
    print('Error')
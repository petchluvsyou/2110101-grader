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
    



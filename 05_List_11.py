inp = input()
digit = [0,0,0,0,0,0,0,0,0,0]
printed = 0
for i in inp:
    if '0'<=i<='9':
        digit[int(i)]+=1
for i in range(10):
    if digit[i]==0:
        if printed:
            print(','+str(i),end='')
        else:
            print(i,end='')
            printed=1
if not printed:
    print("None")
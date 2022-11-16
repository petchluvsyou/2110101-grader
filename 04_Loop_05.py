x = str(input())
y = str(input())
y = [e for e in y]
for i in range(len(y)):
    if y[i]=='\"':
        y[i]=' '
    elif y[i]=='\'':
        y[i]=' '
    elif y[i]=='(':
        y[i]=' '
    elif y[i]==')':
        y[i]=' '
    elif y[i]=='.':
        y[i]=' '
    elif y[i]==',':
        y[i]=' '
y = ''.join(y)
y = y.split(" ")
s = 0
for i in y:
    if x==i:
        s += 1
print(s)
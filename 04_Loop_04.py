k = str(input())
x = [e for e in k]
for i in range(len(x)):
    if x[i]=='(':
        x[i]='['
    elif x[i]=='[':
        x[i]='('
    elif x[i]==')':
        x[i]=']'
    elif x[i]==']':
        x[i]=')'
for i in x:
    print(i,end='')
x = input()
l = len(x)
vowels = ['a','e','i','o','u']
if x[l-1]=='s' or x[l-1]=='x' or x[l-2:l]=='ch':
    print(x+'es')
elif x[l-1]=='y' and x[l-2] not in vowels:
    print(x[:l-1]+'ies')
else:
    print(x+'s')
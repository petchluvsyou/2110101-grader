inp = ''
while(True):
    inp = input()
    if inp=='end':break
    a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for x in inp:
        if 'a'<=x<='z':
            u = a.index(x)
            u+=13
            if u>=26:u-=26
            print(a[u],end='')
        elif 'A'<=x<='Z':
            u=x.lower()
            u = a.index(u)
            u+=13
            if u>=26:u-=26
            print(a[u].upper(),end='')
        else:print(x,end='')
    print()


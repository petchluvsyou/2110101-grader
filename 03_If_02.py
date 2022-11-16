idA, gA, c1A, c2A, c3A = [i for i in input().split()]
idB, gB, c1B, c2B, c3B = [i for i in input().split()]
pA = True
if c1A != 'A':
    pA = False
if c2A > 'C':
    pA = False
if c3A > 'C':
    pA = False
pB = True
if c1B != 'A':
    pB = False
if c2B > 'C':
    pB = False
if c3B > 'C':
    pB = False
if pA == False and pB == False:
    print("None")
elif pA == False:
    print(idB)
elif pB == False:
    print(idA)
else:
    if gA>gB:
        print(idA)
    elif gA<gB:
        print(idB)
    else:
        if c2A<c2B:
            print(idA)
        elif c2A>c2B:
            print(idB)
        else:
            if c3A<c3B:
                print(idA)
            elif c3A>c3B:
                print(idB)
            else:
                print("Both")

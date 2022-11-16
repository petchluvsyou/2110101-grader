def choose(stu1, stu2):
    idA, gA, c1A, c2A, c3A = [i for i in stu1]
    idB, gB, c1B, c2B, c3B = [i for i in stu2]
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
        return []
    elif pA == False:
        return [idB]
    elif pB == False:
        return [idA]
    else:
        if gA>gB:
            return [idA]
        elif gA<gB:
            return [idB]
        else:
            if c2A<c2B:
                return [idA]
            elif c2A>c2B:
                return [idB]
            else:
                if c3A<c3B:
                    return [idA]
                elif c3A>c3B:
                    return [idB]
                else:
                    return [idA,idB]

exec(input())
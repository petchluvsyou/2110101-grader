def missing_digits(t):
    np = []
    inp = t
    digit = [0,0,0,0,0,0,0,0,0,0]
    for i in inp:
        if '0'<=i<='9':
            digit[int(i)]+=1
    for i in range(10):
        if digit[i]==0:
            np.append(i)
    return np
exec(input())
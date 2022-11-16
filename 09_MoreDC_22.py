def read_matrix():
    m = []
    nrows = int(input())
    for k in range(nrows):
        x = input().split()
        r = []
        for e in x:
            r.append( float(e) )
        m.append(r)
    return m

def mult_c(c, A):
    n = len(A)
    m = len(A[0])
    for i in range(n):
        for j in range(m):
            A[i][j]=c*A[i][j]
    return A

def mult(A, B):
    n = len(A)
    m = len(A[0])
    o = len(B[0])
    C = []
    for i in range(n):
        C.append([])
        for j in range(o):
            C[i].append(0)
            for k in range(m):
                C[i][j]+=A[i][k]*B[k][j]
    return C

exec(input().strip())
    
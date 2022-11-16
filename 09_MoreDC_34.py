def pattern1(nrows, ncols):
    ans = []
    c=1
    for i in range(nrows):
        ans.append([])
        for j in range(ncols):
            ans[i].append(c)
            c+=1
    return ans

def pattern2(nrows, ncols):
    ans = []
    c=1
    for i in range(nrows):
        ans.append([])
        for j in range(ncols):
            ans[i].append(0)
    for i in range(ncols):
        for j in range(nrows):
            ans[j][i]=c
            c+=1
    return ans

def pattern3(N):
    ans = []
    c = 1
    x = 0
    for i in range(N):
        ans.append([])
        y = x
        for j in range(N):
            if y:
                ans[i].append(0)
                y-=1
            else:
                ans[i].append(c)
                c+=1
        x+=1
    return ans

def pattern4(N):
    ans = []
    for i in range(N):
        ans.append([])
        for j in range(N):
            ans[i].append(0)
    c = 1
    for i in range(N):
        for j in range(i,-1,-1):
            ans[j][i]=c
            c+=1
    return ans

def pattern5(N):
    ans = []
    for i in range(N):
        ans.append([])
        for j in range(N):
            ans[i].append(0)
    c = 1
    for i in range(N):
        for j in range(N-i):
            ans[j][i+j]=c
            c+=1
    return ans

def pattern6(N):
    ans = []
    for i in range(N):
        ans.append([])
        for j in range(N):
            ans[i].append(0)
    c = 1
    for i in range(N):
        if i%2==0:
            for j in range(N-i):
                ans[j][i+j]=c
                c+=1
        else:
            for j in range(N-i-1,-1,-1):
                ans[j][i+j]=c
                c+=1
    return ans

exec(input().strip())

def RLE(t):
    ans = []
    z = t
    z = z+''
    pv = '#'
    cnt = 0
    for i in z:
        if i!=pv:
            if pv!='#':
                ans.append([pv,cnt])
            cnt = 1
            pv = i
        else:
            cnt = cnt+1
    ans.append([pv,cnt])
    if ans[0][0]=='#':
        return []
    else:
        return ans
exec(input())
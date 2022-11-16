def peaks(x):
    n = x
    peak = []
    for i in range(1,len(n)-1):
        if int(n[i-1])<int(n[i]) and int(n[i])>int(n[i+1]):
            peak.append(i)
    return peak
exec(input())
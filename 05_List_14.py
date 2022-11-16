n = input().split()
peak = 0
for i in range(1,len(n)-1):
    if int(n[i-1])<int(n[i]) and int(n[i])>int(n[i+1]):
        peak+=1
print(peak)
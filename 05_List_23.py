n = int(input())
ans = []
for i in range(n):
    x,y = [float(h) for h in input().split()]
    ans.append([x*x+y*y,i+1,x,y])
ans.sort()
print('#'+str(ans[2][1])+': ('+str(ans[2][2])+', '+str(ans[2][3])+')')
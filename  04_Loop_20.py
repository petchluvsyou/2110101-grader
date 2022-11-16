mi1 = 2e9
ma1 = -2e9
mi2 = 2e9
ma2= -2e9
i=-1
while True:
    i = i+1
    inp = input().split()
    if len(inp)==1:
        break
    xi, yi = [int(e) for e in inp]
    xi = int(xi)
    yi = int(yi)
    if(i%2==0):
        mi1=min(xi,mi1)
        ma1=max(yi,ma1)
        mi2=min(yi,mi2)
        ma2=max(xi,ma2)
    else:
        mi2=min(xi,mi2)
        ma2=max(yi,ma2)
        mi1=min(yi,mi1)
        ma1=max(xi,ma1)
xi = inp[0]
if xi[1]=='i':
    print(mi1,ma1)
else:
    print(mi2,ma2)

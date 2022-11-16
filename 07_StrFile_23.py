inp,yr = input().split()
scores = []
f = open(inp,'r')
for l in f:
    id,score = l.split()
    if yr[2:] == id[:2]:
        scores.append(float(score))
f.close()
scores.sort()
if len(scores)==0:print('No data')
else:
    sum=0
    for s in scores:
        sum+=s
    sum/=len(scores)
    print(str(scores[0]),str(scores[-1]),str(sum))

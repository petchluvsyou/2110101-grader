def distance1(x1, y1, x2, y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5
def distance2(p1, p2):
    x1,y1=p1
    x2,y2=p2
    return ((x1-x2)**2+(y1-y2)**2)**0.5
def distance3(c1, c2):
    x1,y1,r1=c1
    x2,y2,r2=c2
    if ((x1-x2)**2+(y1-y2)**2)**0.5<=r1+r2:
        return ((x1-x2)**2+(y1-y2)**2)**0.5, True
    else:
        return ((x1-x2)**2+(y1-y2)**2)**0.5, False

def perimeter(points):
    sum = 0
    for i in range(len(points)-1):
        sum+=distance2(points[i],points[i+1])
    sum+=distance2(points[len(points)-1],points[0])
    return sum
exec(input().strip())
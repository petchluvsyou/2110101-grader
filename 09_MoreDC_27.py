def knows(R,x,y):
    if y in R[x]: return True
    else: return False

def is_celeb(R,x):
    for z in R:
        if z==x: continue
        if x not in R[z]: return False
    if R[x]==set() or R[x]=={x}: return True
    else: return False

def find_celeb(R):
    for x in R:
        if is_celeb(R,x):return x

def read_relations() :
    R = dict()
    while True:
        d = input().split()
        if len(d) == 1 : break
        x,y = d
        if x not in R: R[x]=set()
        if y not in R: R[y]=set()
        R[x].add(y)
    return R

def main():
    R = read_relations()
    c = find_celeb(R)
    if c == None :
        print('Not Found')
    else:
        print(c)

exec(input().strip())
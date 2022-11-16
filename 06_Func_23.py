def make_int_list(x):
    x = x.split()
    y = []
    for i in x:
        y.append(int(i))
    return y
def is_odd(e):
    if e%2==0:
        return False
    else:
        return True
def odd_list(alist):
    l = []
    for i in alist:
        if is_odd(i):
            l.append(i)
    return l
def sum_square(alist):
    sum=0
    for i in alist:
        sum+=i*i
    return sum
exec(input().strip())
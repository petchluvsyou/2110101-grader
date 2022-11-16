def is_prime(n):
    if n <= 1:
        return False
    for k in range(2,int(n**0.5)+1):
        if n%k == 0:
            return False
    return True

def next_prime(N):
    x = N+1
    while True:
        if is_prime(x):
            return x
        x+=1

def next_twin_prime(N):
    x = N+1
    while True:
        if is_prime(x) and is_prime(x+2):
            return (x,x+2)
        x+=1

exec(input())
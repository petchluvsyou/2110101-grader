def gcd(a,b):
    while b != 0:
        a,b = b, a%b
    return a

def is_coprime(a, b, c):
    if gcd(a,b)==1 or gcd(b,c)==1 or gcd(a,c)==1:
        return True
    else: return False

def primitive_Pythagorean_triples(max_len):
    l = []
    c = 1
    while c<=max_len:
        a = 1
        while a*a<=c*c-a*a:
            b = (c*c-a*a)**(0.5)
            if b == round(b):
                if is_coprime(a,int(b),c):l.append([a,int(b),c])
            a+=1
        c+=1
    return l

exec(input().strip())
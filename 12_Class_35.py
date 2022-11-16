class roman :
    def __init__(self, r):
        foundi = 0
        foundx = 0
        foundc = 0
        sum = 0
        for x in r:
            if x=='I':
                foundi+=1
                sum+=1
            elif x=='V':
                sum+=5-2*foundi
            elif x=='X':
                foundx+=1
                sum+=10-2*foundi
            elif x=='L':
                sum+=50-20*foundx
            elif x=='C':
                foundc+=1
                sum+=100-20*foundx
            elif x=='D':
                sum+=500-200*foundc
            else: sum+=1000-200*foundc
        self.r = sum
    def __lt__(self, rhs):
        return self.r < rhs.r
    def __str__(self):
        x = self.r
        T = ['','M','MM','MMM','MMMM']
        H = ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
        Te = ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
        O = ['','I','II','III','IV','V','VI','VII','VIII','IX']
        return ''.join([T[x//1000],H[x%1000//100],Te[x%100//10],O[x%10]])
    def __int__(self):
        return self.r
    def __add__(self, rhs):
        x = self.r+rhs.r
        T = ['','M','MM','MMM','MMMM']
        H = ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
        Te = ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
        O = ['','I','II','III','IV','V','VI','VII','VIII','IX']
        return roman(''.join([T[x//1000],H[x%1000//100],Te[x%100//10],O[x%10]]))

t, r1, r2 = input().split()
a = roman(r1); b = roman(r2)
if t=='1':print(a<b)
elif t == '2' : print(int(a),int(b))
elif t == '3' : print(str(a),str(b))
elif t == '4' : print(int(a + b))
else : print(str(a + b))
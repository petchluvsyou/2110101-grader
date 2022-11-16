class piggybank:
    def __init__(self):
        self.coins = {}
        self.N = 0
    
    def add(self, v, n):
        if self.N+n>100: return False
        v = float(v)
        if v not in self.coins: self.coins[v] = 0
        self.coins[v] += n
        self.N += n
        return True
    
    def __float__(self):
        sum = 0.0
        for v in self.coins: sum+=v*self.coins[v]
        return sum
    
    def __str__(self):
        ans = []
        L = []
        for v in self.coins: L.append((v,self.coins[v]))
        L.sort()
        for a,b in L: ans.append(str(a)+':'+str(b))
        return '{'+', '.join(ans)+'}'

cmd1 = input().split(';')
cmd2 = input().split(';')
p1 = piggybank(); p2 = piggybank()
for c in cmd1: eval(c)
for c in cmd2: eval(c)
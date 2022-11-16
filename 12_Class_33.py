class piggybank:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0
        self.d = 0
    def add1(self, n):
        self.a+=n
    def add2(self, n):
        self.b+=n
    def add5(self, n):
        self.c+=n
    def add10(self, n):
        self.d+=n
    def __int__(self):
        return self.a+2*self.b+5*self.c+10*self.d
    def __lt__(self, rhs):
        return self.a+2*self.b+5*self.c+10*self.d < rhs.a+2*rhs.b+5*rhs.c+10*rhs.d
    def __str__(self):
        return '{1:'+str(self.a)+', 2:'+str(self.b)+', 5:'+str(self.c)+', 10:'+str(self.d)+'}'

cmd1 = input().split(';')
cmd2 = input().split(';')
p1 = piggybank(); p2 = piggybank()
for c in cmd1: eval(c)
for c in cmd2: eval(c)
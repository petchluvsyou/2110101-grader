class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    def __str__(self):
        return '('+self.value+' '+self.suit+')'
    def next1(self):
        v = ['3','4','5','6','7','8','9','10','J','Q','K','A','2']
        s = ['club','diamond','heart','spade']
        sum = v.index(self.value)*4+s.index(self.suit)
        sum+=1
        if sum==52:sum=0
        return Card(v[sum//4],s[sum%4])
    def next2(self):
        v = ['3','4','5','6','7','8','9','10','J','Q','K','A','2']
        s = ['club','diamond','heart','spade']
        sum = v.index(self.value)*4+s.index(self.suit)
        sum+=1
        if sum==52:sum=0
        self.value = v[sum//4]
        self.suit=  s[sum%4]

n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))
for i in range(n):
    print(cards[i].next1())
print("----------")
for i in range(n):
    print(cards[i])
print("----------")
for i in range(n):
    cards[i].next2()
    cards[i].next2()
    print(cards[i])
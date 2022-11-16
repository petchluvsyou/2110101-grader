class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    def __str__(self):
        return '('+self.value+' '+self.suit+')'
    def getScore(self):
        v = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10}
        return v[self.value]
    def sum(self, other):
        return (self.getScore()+other.getScore())%10
    def __lt__(self, rhs):
        v = ['3','4','5','6','7','8','9','10','J','Q','K','A','2']
        s = ['club','diamond','heart','spade']
        return (v.index(self.value),s.index(self.suit))<(v.index(rhs.value),s.index(rhs.suit))

n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))
for i in range(n):
    print(cards[i].getScore())
print("----------")
for i in range(n-1):
    print(Card.sum(cards[i], cards[i+1]))
print("----------")
cards.sort()
for i in range(n):
    print(cards[i])
card = input().split()
n = len(card)
x = input()
for i in x:
    if i=='C':
        card = card[n//2:]+card[:n//2]
    elif i=='S':
        temp = []
        for i in range(n//2):
            temp.append(card[i])
            temp.append(card[n//2+i])
        card = temp
for i in card:
    print(i, end=' ')

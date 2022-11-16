x = input()
y = int(x[3:32:7])
z = int(x[7:28:5])
y = y+z
y = (y%10000)//10
z = (y//100+(y//10)%10+y%10)%10
m = str(y)
k = ""
for i in range(3-len(m)):
    k = k+'0'
k = k+m
c = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
c = c[z]
print(str(k)+c)

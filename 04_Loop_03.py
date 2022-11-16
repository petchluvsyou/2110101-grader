x = input()
s = input()
c = 0
if len(x)!=len(s):
    print("Incomplete answer")
else:
    for i in range(len(x)):
        if x[i]==s[i]:
            c += 1
    print(c)
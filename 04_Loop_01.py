sum = 0
n = 0
while True:
    x = input()
    if x != "q":
        x = float(x)
    else:
        break
    sum += x
    n += 1
if n==0:
    print("No Data")
else:
    print(round(sum/n,2))
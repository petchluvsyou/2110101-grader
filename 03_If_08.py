d = int(input())
m = int(input())
y = int(input())
month = [31,28,31,30,31,30,31,31,30,31,30,31]
sum = d
m = m-1
while m!=0:
    m = m-1
    sum = sum+month[m]
    if m==1 and ((y%4==3 and (y-543)%100!=0) or (y-543)%400==0):
        sum = sum+1
print(sum)
def read_date():
    d,m,y = input().split()
    d = int(d)
    y = int(y)
    month = ["Jan", "Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    m = month.index(m)+1
    return [d,m,y]
def zodiac(d1,m1):
    z1 = ''
    if   d1 >= 22 and m1==3  or d1 <=21 and m1==4  : z1 = "Aries"
    elif d1 >= 22 and m1==4  or d1 <=21 and m1==5  : z1 = "Taurus"
    elif d1 >= 22 and m1==5  or d1 <=21 and m1==6  : z1 = "Gemini"
    elif d1 >= 22 and m1==6  or d1 <=21 and m1==7  : z1 = "Cancer"
    elif d1 >= 22 and m1==7  or d1 <=21 and m1==8  : z1 = "Leo"
    elif d1 >= 22 and m1==8  or d1 <=21 and m1==9  : z1 = "Virgo"
    elif d1 >= 22 and m1==9  or d1 <=21 and m1==10 : z1 = "Libra"
    elif d1 >= 22 and m1==10 or d1 <=21 and m1==11 : z1 = "Scorpio"
    elif d1 >= 22 and m1==11 or d1 <=21 and m1==12 : z1 = "Sagittarius"
    elif d1 >= 22 and m1==12 or d1 <=20 and m1==1  : z1 = "Capricorn"
    elif d1 >= 21 and m1==1  or d1 <=20 and m1==2  : z1 = "Aquarius"
    elif d1 >= 21 and m1==2  or d1 <=21 and m1==3  : z1 = "Pisces"
    return z1
def days_in_feb(y1):
    if y1 % 400 == 0 or y1 % 100 != 0 and y1%4 == 0 :
        return 29
    else:
        return 28
def days_in_month(m,y):
    months = [31,28,31,30,31,30,31,31,30,31,30,31]
    if m!=2:
        return months[m-1]
    else:
        return days_in_feb(y)
def days_in_between(d1,m1,y1,d2,m2,y2):
    months = [31,28,31,30,31,30,31,31,30,31,30,31]
    days1=d1
    days2=d2
    for i in range(m1-1):
        if i!=1:
            days1+=months[i]
        else:
            days1+=days_in_feb(y1)
    for i in range(m2-1):
        if i!=1:
            days2+=months[i]
        else:
            days2+=days_in_feb(y2)
    days = days2 + (365-28+days_in_feb(y1)-days1-1)
    for i in range(y1+1,y2):
        days+=365-28+days_in_feb(i)
    return days
def main() :
    d1,m1,y1 = read_date()
    d2,m2,y2 = read_date()
    z2=zodiac(d1,m1)
    z3=zodiac(d2,m2)
    print(z2,z3)
    print(days_in_between(d1,m1,y1,d2,m2,y2))
exec(input().strip())
 
 
    
 
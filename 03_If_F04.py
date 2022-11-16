def is_mobile_number(number):
    x = number
    c = True
    if len(x)!=10:
        c = False
    for i in x:
        if not('9'>=i>='0'):
            c = False
    if c==True:
        if x[0:2]=="06" or x[0:2]=="08" or x[0:2]=="09":
            return True
        else:
            return False
    else:
        return False
exec(input())
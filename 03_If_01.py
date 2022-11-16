from http.client import OK


x = input()
if "41">x>"19" and len(x)==2:
    if "5">x[0]>"0" and '9'>=x[1]>='0':
        print("OK")
    else:
        print("Error")
elif x=="01" or x=="02" or x=="51" or x=="53" or x=="55" or x=="58":
    print("OK")
else:
    print("Error")
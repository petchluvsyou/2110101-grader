n = str(input())

x = (11-(13*int(n[0])+12*int(n[1])+11*int(n[2])+10*int(n[3])+9*int(n[4])+8*int(n[5])+7*int(n[6])+6*int(n[7])+5*int(n[8])+4*int(n[9])+3*int(n[10])+2*int(n[11]))%11)%10

n=n+str(x)

print(n[0:1]+" "+n[1:5]+" "+n[5:10]+" "+n[10:12]+" "+n[12])
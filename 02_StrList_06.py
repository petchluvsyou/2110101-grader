x = input()
x = x[1:len(x)-1]
y = x.split(", ")
z = input()
z = z[1:len(z)-1]
w = z.split(", ")

print("["+str(float(y[0]))+", "+str(float(y[1]))+", "+str(float(y[2]))+"] + ["+str(float(w[0]))+", "+str(float(w[1]))+", "+str(float(w[2]))+"] = ["+str(float(y[0])+float(w[0]))+", "+str(float(y[1])+float(w[1]))+", "+str(float(y[2])+float(w[2]))+"]")

def add_vector(u, v):
    x = str(u)
    x = x[1:len(x)-1]
    y = x.split(", ")
    z = str(v)
    z = z[1:len(z)-1]
    w = z.split(", ")

    return "["+str(float(y[0])+float(w[0]))+", "+str(float(y[1])+float(w[1]))+", "+str(float(y[2])+float(w[2]))+"]"

exec(input())
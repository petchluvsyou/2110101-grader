import numpy as np

def read_data():
    w = [float(e) for e in input().split()]
    weight = np.array(w)
    n = int(input())
    data = np.ndarray((n, 4), int)
    for i in range(n):
        data[i] = [int(e) for e in input().split()]
    return weight, data

def report_lower_than_mean(weight, data):
    if data[np.sum(weight*data[:,1:],axis=1)<np.mean(np.sum(weight*data[:,1:],axis=1))][:,0].shape[0]!=0: print(str(data[np.sum(weight*data[:,1:],axis=1)<np.mean(np.sum(weight*data[:,1:],axis=1))][:,0])[1:-1].replace(' ',', '))
    else: print('None')

exec(input().strip())
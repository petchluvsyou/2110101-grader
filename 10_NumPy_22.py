import numpy as np

def mult_table(nrows, ncols):
    return (np.arange(1,nrows+1)*np.ones((ncols,nrows),int)).T*np.arange(1,ncols+1)[:]

exec(input().strip())
# Reference kernel

import numpy as np

def w_r(x, a, mu, X):
    
    dimX = X.shape[0]
    
    w_r = np.zeros(dimX, dtype=float)

    if x + a <= -1:
        w_r[0] = 1
    elif x + a == 0:
        w_r[0] = 2/3
        w_r[1] = 1/3
    elif x + a == dimX - 1:
        w_r[dimX - 2] = 1/3
        w_r[dimX - 1] = 2/3
    elif x + a >= dimX:
        w_r[dimX - 1] = 1
    else:
        w_r[x + a - 1] = 1/3
        w_r[x + a] = 1/3
        w_r[x + a + 1] = 1/3

    return w_r
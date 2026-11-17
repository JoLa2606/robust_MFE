# Reference kernel

import numpy as np

def w_r(x, a, mu, X):
    
    beta = 0.7
    epsilon_0 = 0.1 
    epsilon_1 = 0.2

    dimX = X.shape[0]
    
    w_r = np.zeros(dimX, dtype=float)

    if x == 0:
        if a == 1:
            w_r[1] = 1 - beta * mu[1]
            w_r[0] = 1 - w_r[1]
        elif a == 0:
            w_r[1] = epsilon_0
            w_r[0] = 1 - w_r[1]
        else:
            w_r[0] = 1
    else:
        if a == -1:
            w_r[0] = 1 - beta * mu[1]
            w_r[1] = 1 - w_r[0]
        elif a == 0:
            w_r[0] = epsilon_1
            w_r[1] = 1 - w_r[0]
        else:
            w_r[1] = 1

    return w_r
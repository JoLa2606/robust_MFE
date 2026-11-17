# Reward function

import numpy as np

def r(x, a, y, mu, X):

    dimX = X.shape[0]
    
    R = 1000
    C_1 = 2000
    C_2 = 50
    
    r = (R - C_1 * mu[1]) * y - np.abs(a) * C_2

    return r
# Reward function

import numpy as np

def r(x, a, y, mu, X):

    dimX = X.shape[0]
    
    c = 0.0000001
    
    r = (1 - 1 / ((dimX - 1) / 2) * np.abs(y - (dimX - 1) / 2)) - np.abs(a) / dimX - np.log(mu[y] + c)

    return r
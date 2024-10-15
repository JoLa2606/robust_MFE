# Expected reward given the worst-case kernel at t = 1

import numpy as np

from r import r
from w_p1 import w_p1

def J_1(x, a, mu, X, lmbd):

    dimX = X.shape[0]

    J_1 = 0
    wp1 = w_p1(x, a, mu, X, lmbd)

    for i in range(dimX):
        J_1 = J_1 + wp1[i] * r(x, a, X[i], mu, X)

    return J_1
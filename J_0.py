# Expected reward given the worst-case kernel at t = 0

import numpy as np

from r import r
from V_1 import V_1
from w_p0 import w_p0

def J_0(x, a, mu, X, A, lmbd):

    dimX = X.shape[0]

    J_0 = 0
    wp0 = w_p0(x, a, mu, X, A, lmbd)

    for i in range(dimX):
        J_0 = J_0 + wp0[i] * (r(x, a, X[i], mu[0,:], X) + V_1(x, mu[1, :], X, A, lmbd))

    return J_0
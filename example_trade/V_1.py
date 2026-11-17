# Expected reward given the optimal policy at t = 1

import numpy as np

from J_1 import J_1
from w_pi1 import w_pi1

def V_1(x, mu, X, A, lmbd):

    dimA = A.shape[0]
    
    V_1 = 0

    wpi1 = w_pi1(x, mu, X, A, lmbd)

    for i in range(dimA):
        V_1 = V_1 + wpi1[i] * J_1(x, A[i], mu, X, lmbd)

    return V_1
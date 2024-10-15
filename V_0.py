# Expected reward given the optimal policy at t = 0

import numpy as np

from J_0 import J_0
from w_pi0 import w_pi0

def V_0(x, mu, X, A, lmbd):

    dimA = A.shape[0]
    
    V_0 = 0

    wpi0 = w_pi0(x, mu, X, A, lmbd)

    for i in range(dimA):
        V_0 = V_0 + wpi0[i] * J_0(x, A[i], mu, X, A, lmbd)

    return V_0

# def V_0(x, mu, X, A, lmbd):

#     return w_pi0(x, mu, X, A, lmbd) * J_0(x, A[0], mu, X, A, lmbd) + (1 - w_pi0(x, mu, X, A, lmbd)) * J_0(x, A[1], mu, X, A, lmbd)

# import numpy as np

# from J_0 import J_0
# from w_pi0 import w_pi0
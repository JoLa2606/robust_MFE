# Calculates the worst-case kernel weights at t = 0 in the Wasserstein ball around the reference kernel

import numpy as np

from scipy.stats import wasserstein_distance

from r import r
from V_1 import V_1
from w_r import w_r
from worstCaseWeightsWithWasserstein import worstCaseWeightsWithWasserstein

def w_p0(x, a, mu, X, A, lmbd):

    dimX = X.shape[0]

    w_ref = w_r(x, a, mu[0,:], X)
    w_p0  = list(w_ref)

    rew = np.zeros(dimX, dtype=float)
    for i in range(dimX):
        rew[i] = r(x, a, X[i], mu[0,:], X) + V_1(x, mu[1,:], X, A, lmbd)


    # Obtains the worst-case kernel inside the wasserstein ball around the reference kernel
    w_p0 = worstCaseWeightsWithWasserstein(w_ref, rew, lmbd, X)

    return w_p0
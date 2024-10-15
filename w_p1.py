# Calculates the worst-case kernel weights at t = 1 in the Wasserstein ball around the reference kernel

import numpy as np

from scipy.stats import wasserstein_distance

from r import r
from w_r import w_r
from worstCaseWeightsWithWasserstein import worstCaseWeightsWithWasserstein

def w_p1(x, a, mu, X, lmbd):

    dimX = X.shape[0]

    w_ref = w_r(x, a, mu, X)
    w_p1  = list(w_ref)

    rew = np.zeros(dimX, dtype=float)
    for i in range(dimX):
        rew[i] = r(x, a, X[i], mu, X)

    # Obtains the worst-case kernel inside the wasserstein ball around the reference kernel
    w_p1 = worstCaseWeightsWithWasserstein(w_ref, rew, lmbd, X)

    return w_p1
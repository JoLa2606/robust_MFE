# Calculates the optimal policy weights at t = 0

import numpy as np

from J_0 import J_0

def w_pi0(x, mu, X, A, lmbd):

    dimA = A.shape[0]

    w_pi0 = np.ones(dimA, dtype=float)
    w_pi0 = w_pi0 / dimA

    epsln = 0.0001
    maxSteps = 1000
    step = 1
    stepSize = 0.001
    temp  = np.ones(dimA, dtype=float)

    J0 = np.zeros(dimA, dtype=float)
    for i in range(dimA):
        J0[i] = J_0(x, A[i], mu, X, A, lmbd)

    # Gets all indices that obtain the maximal value of J0
    max_indices = np.where(J0 == np.max(J0))[0]

    while np.linalg.norm(np.subtract(w_pi0, temp)) > epsln and step < maxSteps:
        temp = list(w_pi0)
        stepSize = lmbd
        step = step + 1

        w_pi0 = np.zeros(dimA, dtype=float)

        # Puts all the weight on the points with the maximal expected reward
        for i in max_indices:
            w_pi0[i] = 1 / max_indices.shape[0]

        if np.sum(w_pi0) == 0:
            print("w_pi0 == 0")

    return w_pi0
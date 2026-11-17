# Calculates the optimal policy weights at t = 1

import numpy as np

from J_1 import J_1

def w_pi1(x, mu, X, A, lmbd):

    dimA = A.shape[0]

    w_pi1 = np.ones(dimA, dtype=float)
    w_pi1 = w_pi1 / dimA

    epsln = 0.0001
    maxSteps = 1000
    step = 1
    stepSize = 0.001
    temp  = np.ones(dimA, dtype=float)

    J1 = np.zeros(dimA, dtype=float)
    for i in range(dimA):
        J1[i] = J_1(x, A[i], mu, X, lmbd)
    
    # Gets all indices that obtain the maximal value of J1
    max_indices = np.where(J1 == np.max(J1))[0]

    while np.linalg.norm(np.subtract(w_pi1, temp)) > epsln and step < maxSteps:
        temp = list(w_pi1)
        stepSize = lmbd
        step = step + 1

        w_pi1 = np.zeros(dimA, dtype=float)
        
        # Puts all the weight on the points with the maximal expected reward
        for i in max_indices:
            w_pi1[i] = 1 / max_indices.shape[0]

        if np.sum(w_pi1) == 0:
            print("w_pi1 == 0")

    return w_pi1
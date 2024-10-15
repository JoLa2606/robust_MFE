# How to create the graphs:
# 1. Use findMFE.py
# 2. Use SortData.py
# 3. Use createGraphs.py
# 4. Use createGraphs_wp.py
# 5. Use createGraphs_wpi.py

# Main function for the iterative scheme to find the MFE

import numpy as np

from V_0 import V_0
from w_p0 import w_p0
from w_p1 import w_p1
from w_pi0 import w_pi0
from w_pi1 import w_pi1

# States
X = np.zeros(5, dtype=int)
dimX = X.shape[0]
for i in range(dimX):
    X[i] = i

# Actions
A = np.zeros(3, dtype=int)
A[0] = -1
A[2] = 1
dimA = A.shape[0]

# State-Measure Flow
mu = np.zeros((2, dimX), dtype=float)
mu[0, 0] = 0.2
mu[0, 1] = 0.1
mu[0, 2] = 0.05
mu[0, 3] = 0.25
mu[0, 4] = 0.4
mu[1, 0] = 0.2
mu[1, 1] = 0.2
mu[1, 2] = 0.2
mu[1, 3] = 0.2
mu[1, 4] = 0.2

mu_init = list(mu)

mu2 = np.zeros(dimX, dtype=float)

# Uncertainty Parameter
lmbd = 0.1
lmbdRange = 4

# Parameters for the iterative scheme
epsln = 0.0001
maxSteps = 1000
step = 1

# Weights of the kernels
wpi0 = np.zeros((dimX, dimA), dtype=float)
wp0 = np.zeros((dimX, dimA, dimX), dtype=float)
wpi1 = np.zeros((dimX, dimA), dtype=float)
wp1 = np.zeros((dimX, dimA, dimX), dtype=float)
V = 0

with open('output_mu0.txt', 'w') as output_mu0, open('output_mu1.txt', 'w') as output_mu1, open('output_mu2.txt', 'w') as output_mu2, open('output_wpi0.txt', 'w') as output_wpi0, open('output_wpi1.txt', 'w') as output_wpi1, open('output_wp0.txt', 'w') as output_wp0, open('output_wp1.txt', 'w') as output_wp1, open('output_V.txt', 'w') as output_V:
    for i in range(lmbdRange, -1, -1):
        
        # initialize lambda and mu
        lmbd = 1 / (i + 1)
        if i == lmbdRange:
            lmbd = 0
        mu = np.array(list(mu_init))
        temp = np.ones(dimX, dtype=float)
        step = 1

        # Iterative scheme for different levels of uncertainty
        while np.linalg.norm(np.subtract(mu[1, :], temp)) > epsln and step < maxSteps:
            temp = list(mu[1, :])
            
            # Weights of the optimal policy at t = 0
            for i in range(dimX):
                wpi0[i, :] = w_pi0(X[i], mu, X, A, lmbd)

            # Weights of the worst-case kernel at t = 0
            for i in range(dimX):
                for j in range(dimA):
                    wp0[i, j, :] = w_p0(X[i], A[j], mu, X, A, lmbd)

            # Weights of the state-measure flow
            for i in range(dimX):
                mu[1, i] = 0
                for j in range(dimX):
                    for k in range(dimA):
                        mu[1, i] = mu[1, i] + mu[0, j] * wpi0[j, k] * wp0[j, k, i]

            step = step + 1

        # Value function and weights of the optimal policy and worst-case kernel at t = 1
        V = 0
        for i in range(dimX):
            wpi1[i, :] = w_pi1(X[i], mu[1, :], X, A, lmbd)
            V = V + mu[0, i] * V_0(X[i], mu, X, A, lmbd)

            for j in range(dimA):
                wp1[i, j, :] = w_p1(X[i], A[j], mu[1, :], X, lmbd)

        # Weights of the state-measure flow at time t = 2
        for i in range(dimX):
            mu2[i] = 0
            for j in range(dimX):
                for k in range(dimA):
                    mu2[i] = mu2[i] + mu[1, j] * wpi1[j, k] * wp1[j, k, i]
        
        # output data as txt-file
        output_mu0.write(f"{lmbd:.10f} {mu[0, 0]:.10f} {mu[0, 1]:.10f} {mu[0, 2]:.10f} {mu[0, 3]:.10f} {mu[0, 4]:.10f}\n")
        output_mu1.write(f"{lmbd:.10f} {mu[1, 0]:.10f} {mu[1, 1]:.10f} {mu[1, 2]:.10f} {mu[1, 3]:.10f} {mu[1, 4]:.10f}\n")
        output_mu2.write(f"{lmbd:.10f} {mu2[0]:.10f} {mu2[1]:.10f} {mu2[2]:.10f} {mu2[3]:.10f} {mu2[4]:.10f}\n")

        for i in range(dimX):
            output_wpi0.write(f"{lmbd:.10f} {X[i]:.10f} {wpi0[i, 0]:.10f} {wpi0[i, 1]:.10f} {wpi0[i, 2]:.10f}\n")
            output_wpi1.write(f"{lmbd:.10f} {X[i]:.10f} {wpi1[i, 0]:.10f} {wpi1[i, 1]:.10f} {wpi1[i, 2]:.10f}\n")
            for j in range(dimA):
                output_wp0.write(f"{lmbd:.10f} {X[i]:.10f} {A[j]:.10f} {wp0[i, j, 0]:.10f} {wp0[i, j, 1]:.10f} {wp0[i, j, 2]:.10f} {wp0[i, j, 3]:.10f} {wp0[i, j, 4]:.10f}\n")
                output_wp1.write(f"{lmbd:.10f} {X[i]:.10f} {A[j]:.10f} {wp1[i, j, 0]:.10f} {wp1[i, j, 1]:.10f} {wp1[i, j, 2]:.10f} {wp1[i, j, 3]:.10f} {wp1[i, j, 4]:.10f}\n")

        output_V.write(f"{lmbd:.10f} {V:.10f}\n")

output_mu0.closed
output_mu1.closed
output_mu2.closed
output_wpi0.closed
output_wpi1.closed
output_wp0.closed
output_wp1.closed
output_V.closed

print("Finished")
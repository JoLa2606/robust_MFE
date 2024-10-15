# finds the minimizing weights in the Wasserstein ball

import numpy as np
from scipy.optimize import minimize
from scipy.stats import wasserstein_distance

def worstCaseWeightsWithWasserstein(p, r, epsilon, X):
    n = len(p)
    
    # Define the constraint function for the Wasserstein distance
    def wassersteinConstraint(q):
        distance = wasserstein_distance(X, X, p, q)
        return epsilon - distance  # Must be non-negative
    
    # Constraints definition
    constraints = [
        {'type': 'eq', 'fun': lambda q: np.sum(q) - 1},  # Sum of q_i must be 1
        {'type': 'ineq', 'fun': wassersteinConstraint}  # q within Wasserstein ball
    ]
    
    # Bounds for the variables q_i must be non-negative
    bounds = [(0, None)] * n
    
    # Initial guess for the optimization
    q0 = p
    
    # Solve the optimization problem
    result = minimize(lambda q: np.dot(q, r), q0, bounds=bounds, constraints=constraints, method='SLSQP')
    
    if result.success:
        return result.x
    else:
        print('p')
        print(p)
        print('r')
        print(r)
        raise ValueError(f"Optimization failed: {result.message}")
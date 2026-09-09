import numpy as np
from scipy.optimize import linprog
C = [-30, -20, -50]


Aeq = [
        [2, -3, 0],
        [0, 5, -2],
]

Beq = [0, 0]

Aub = [
    [2, 3, 5],
    [4, 2, 7],
    [1, 1/2, 1/3],
    [-1, 0, 0],
    [0, -1, 0],
    [0, 0, -1]
]
Bub = [4000, 6000, 1500, -200, -200, -150]

res = linprog(C, A_eq=Aeq, b_eq=Beq, A_ub=Aub, b_ub=Bub, method='highs')

if res.success:
    print("Optimization successful!")
    print(f"Optimal value for x1: {res.x[0]:.1f}")
    print(f"Optimal value for x2: {res.x[1]:.1f}")
    print(f"Optimal value for x3: {res.x[2]:.1f}")
    print(f"Maximum value of the objective function: {-res.fun:.1f}")
else:
    print("Optimization failed:", res.message)
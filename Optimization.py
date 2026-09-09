import numpy as np
import scipy.optimize as linprog

p = [-5, -4]

A = [
    [6, 4],
    [1, 2],
    [0, 1],
    [-1, 1],
]

b = [24, 6, 2, 1]

result = linprog.linprog(p, A_ub=A, b_ub=b, method='highs')
if result.success:
    print("Optimal solution found:")
    print(f"Optimal value for x2: {result.x[1]:.4f}")
    print(f"Optimal value for x1: {result.x[0]:.4f}")
    print(f"Optimal objective value: {-result.fun:.4f}")
else:
    print("Optimization failed:")
    print(result.message)

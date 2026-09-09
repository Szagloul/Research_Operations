import numpy as np
from scipy.optimize import linprog
  #  x1 x2 x3 x4 y1 y2 y3 y4 y5
  #  maximize y5
C = [0, 0, 0, 0, 0, 0, 0, 0, -1]


A_ub = [
        [1,1,0,1,1,0,0,0,0]
]

B_ub = [10000]

Aeq = [
       [.5, .6, -1, .4, 1.065, -1, 0, 0, 0],
       [.3, .2, .8, .6, 0, 1.065, -1, 0, 0],
       [1.8, 1.5, 1.9, 1.8, 0, 0, 1.065, -1, 0],
       [1.2, 1.3, .8, .95, 0, 0, 0, 1.065, -1]
]
Beq = [0, 0, 0, 0]

res = linprog(C, A_eq=Aeq, b_eq=Beq, A_ub=A_ub, b_ub=B_ub, method='highs')

if res.success:
    print("Optimization successful!")
    print(f"Optimal value for x1: {res.x[0]:.1f}")
    print(f"Optimal value for x2: {res.x[1]:.1f}")
    print(f"Optimal value for x3: {res.x[2]:.1f}")
    print(f"Optimal value for x4: {res.x[3]:.1f}")
    print(f"Optimal value for y1: {res.x[4]:.1f}")
    print(f"Optimal value for y2: {res.x[5]:.1f}")
    print(f"Optimal value for y3: {res.x[6]:.1f}")
    print(f"Optimal value for y4: {res.x[7]:.1f}")
    print(f"Optimal value for y5: {res.x[8]:.1f}")
    print(f"Maximum value of the objective function: {-res.fun:.1f}")
else:
    print("Optimization failed:", res.message)
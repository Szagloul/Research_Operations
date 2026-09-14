import numpy as np
from scipy.optimize import linprog

c = [-1.0167, -1.1167, -1.1667, -1.1167, -1.06, -1.16, -1.11]

Aeq = [
  # x11 x12 x21 x22 x31 x32 x33
    [1,  0,  0,  0,  -1,  0,  0],   # x11 -x31 = 0,
    [0,  1,  -1,  0,  0,  0,  0],   # x12 -x21 = 0
    [0,  0,  2,  0,   0,  -1, 0],   # 2x21 - x32 = 0
    [0,  0,  0,  3,   0,  0,  -2]   # 3x22 - 2x33 = 0
]

Beq = [0, 0, 0, 0]


Aub = [
  # x11 x12 x21 x22 x31 x32 x33
    [1,  1,  0,  0,  0,  0,  0],  # x11 + x12 <= 300000
    [0,  0,  1,  1,  0,  0,  0],  # x21 + x22 <= 120000
    [0,  0,  0,  0,  1,  1,  1],  # x31 + x32 + x33 <= 150000
]

Bub = [300000, 120000, 150000]

res = linprog(c, A_ub=Aub, b_ub=Bub, A_eq=Aeq, b_eq=Beq, method="highs")

if res.success:
    print("Optimization successful!")
    print(f"Optimal value for x11: {res.x[0]:.2f}")
    print(f"Optimal value for x12: {res.x[1]:.2f}")
    print(f"Optimal value for x21: {res.x[2]:.2f}")
    print(f"Optimal value for x22: {res.x[3]:.2f}")
    print(f"Optimal value for x31: {res.x[4]:.2f}")
    print(f"Optimal value for x32: {res.x[5]:.2f}")
    print(f"Optimal value for x33: {res.x[6]:.2f}")
    print(f"Maximum value of the objective function: {-res.fun:.2f}")
else:
    print("Optimization failed:", res.message)
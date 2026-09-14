import numpy as np
from scipy.optimize import linprog

c = [-48.5, -10, -18.5]

Aub = [
  # x1  x2   x3
    [-.3,  1,  0],   # .3x1 - x2 >= 25
    [-.1,  0,  0],   # .1x1 >= 25
    [0,  -.8,  1],   # .8x2 - x3 >= 25
    [0,    0,  -.95], # .95x3 >= 25
    [1,    0,  0],   # x1 <= 4000
]


Bub = [-25, -25, -25, -25, 4000]

res = linprog(c, A_ub=Aub, b_ub=Bub, method="highs")

if res.success:
    print("Optimization successful!")
    print(f"Optimal value for x1: {res.x[0]:.2f}")
    print(f"Optimal value for x2: {res.x[1]:.2f}")
    print(f"Optimal value for x3: {res.x[2]:.2f}")
    print(f"Maximum value of the objective function: {-res.fun:.2f}")
else:
    print("Optimization failed:", res.message)
import numpy as np
from scipy.optimize import linprog


c = [30, 30, 30, 28, 28, 28, 0.90, 0.90, 0.90, 0.75, 0.75, 0.75]

Aeq = [
    # A1 - I1 = 500
    [1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0],

    # I1 + A2 - I2 = 5000
    [0, 1, 0, 0, 0, 0, 1, -1, 0, 0, 0, 0],

    # I2 + A3 - I3 = 750
    [0, 0, 1, 0, 0, 0, 0, 1, -1, 0, 0, 0],

    # B1 - I4 = 1000
    [0, 0, 0, 1, 0, 0, 0, 0, 0, -1, 0, 0],

    # I4 + B2 - I5 = 1200
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, -1, 0],
    
    # I5 + B3 - I6 = 1200
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, -1],
]

Beq = [500, 500, 750, 1000, 1200, 1200]


Aub = [
    # (4/3)A1 + B1 <= 3000 (June Capacity)
    [4 / 3, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    # (4/3)A2 + B2 <= 3500 (July Capacity)
    [0, 4 / 3, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    # (4/3)A3 + B3 <= 3000 (August Capacity)
    [0, 0, 4 / 3, 0, 0, 1, 0, 0, 0, 0, 0, 0],
]

Bub = [3000, 3500, 3000]

# Variable bounds (all variables >= 0)
bounds = [(0, None) for _ in range(12)]

res = linprog(c, A_ub=Aub, b_ub=Bub, A_eq=Aeq, b_eq=Beq, bounds=bounds, method="highs")

if res.success:
    print("Optimization successful!")
    print(f"Optimal production for A (June, July, Aug): {res.x[0]:.2f}, {res.x[1]:.2f}, {res.x[2]:.2f}")
    print(f"Optimal production for B (June, July, Aug): {res.x[3]:.2f}, {res.x[4]:.2f}, {res.x[5]:.2f}")
    print(f"Ending inventory for A (June, July, Aug): {res.x[6]:.2f}, {res.x[7]:.2f}, {res.x[8]:.2f}")
    print(f"Ending inventory for B (June, July, Aug): {res.x[9]:.2f}, {res.x[10]:.2f}, {res.x[11]:.2f}")
    print(f"Minimum total cost: ${res.fun:.2f}")
else:
    print("Optimization failed:", res.message)
import numpy as np
import matplotlib.pyplot as plt

N = 10000

# 1. Generate N random x and y coordinates between -1 and 1
x = np.random.uniform(-1, 1, N)
y = np.random.uniform(-1, 1, N)

# 2. Distance squared from origin
d_squared = x**2 + y**2

# 3. Boolean mask for points inside the unit circle
inside = d_squared <= 1

# 4. Calculate pi estimate
pi_estimate = 4 * np.sum(inside) / N
print(f"Estimated Pi: {pi_estimate}")
print(f"Actual Pi: {np.pi}")

# 5. Optional visualization
fig, ax = plt.subplots(figsize=(6, 6))
ax.scatter(x[inside], y[inside], color="blue", s=1, label="Inside Circle")
ax.scatter(x[~inside], y[~inside], color="red", s=1, label="Outside Circle")
ax.set_aspect("equal")
ax.legend()
plt.show()
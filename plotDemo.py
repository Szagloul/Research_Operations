import numpy as np
import matplotlib.pyplot as plt

# 1. Define domain using linspace
x = np.linspace(-4, 4, 1000)

# 2. Standard normal distribution probability density function (PDF)
y = (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * x**2)

# 3. Create plot using explicit figure/axes objects
fig, ax = plt.subplots()
ax.plot(x, y, label="Standard Normal PDF", color="blue")
ax.set_title("Standard Normal Distribution")
ax.set_xlabel("x")
ax.set_ylabel("Probability Density")
ax.legend()
ax.grid(True)
plt.show()
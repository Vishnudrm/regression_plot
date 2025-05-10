import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parameters
mu = 0    # mean
sigma = 1  # standard deviation

# Values
x = np.linspace(-4, 4, 1000)
y = norm.pdf(x, mu, sigma)

# Plot
plt.plot(x, y, color='red')
plt.title('Normal Distribution (μ=0, σ=1)')
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.grid(True)
plt.show()

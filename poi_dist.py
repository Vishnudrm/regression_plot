import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

# Parameter
mu = 4  # mean number of events

# Values
x = np.arange(0, 15)
y = poisson.pmf(x, mu)

# Plot
plt.plot(x, y, marker='o', linestyle='-', color='green')
plt.title('Poisson Distribution (μ=4)')
plt.xlabel('Number of Events')
plt.ylabel('Probability')
plt.grid(True)
plt.show()

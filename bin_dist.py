import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

# Parameters
n = 20  # number of trials
p = 0.5  # probability of success

# Values
x = np.arange(0, n + 1)
y = binom.pmf(x, n, p)

# Plot
plt.plot(x, y, marker='o', linestyle='-', color='blue')
plt.title('Binomial Distribution (n=20, p=0.5)')
plt.xlabel('Number of Successes')
plt.ylabel('Probability')
plt.grid(True)
plt.show()

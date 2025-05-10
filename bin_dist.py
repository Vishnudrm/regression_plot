import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

# Get user input
n = int(input("Enter the number of trials (n): "))
p = float(input("Enter the probability of success (p between 0 and 1): "))

# Values
x = np.arange(0, n + 1)
y = binom.pmf(x, n, p)

# Plot
plt.plot(x, y, marker='o', linestyle='-', color='blue')
plt.title(f'Binomial Distribution (n={n}, p={p})')
plt.xlabel('Number of Successes')
plt.ylabel('Probability')
plt.grid(True)
plt.show()

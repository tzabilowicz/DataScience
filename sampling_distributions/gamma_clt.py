"""
Example 1:
X_1, X_2, ... , X_30 are all drawn from a gamma distribution with r=5 and
lam=2. Use the central limit theorem to estimate P(X_bar > 3).
"""
import numpy as np
import matplotlib.pyplot as plt
plt.style.use("ggplot")

# Distribution parameters
r = 5
lam = 2

S = 30
N = 1000
X_bar = []

for i in range(N):
    sample = np.random.gamma(shape=r, scale=1/lam, size=30)
    X_bar.append(np.mean(sample))
    
print(f"X_bar mean: {np.mean(X_bar)}")
print(f"X_bar std:  {np.std(X_bar)}")

plt.hist(X_bar, bins=20)
plt.show()

# Estimate the probability
count = np.sum(np.array(X_bar) > 3)
p = count / len(X_bar)
print(p)
import numpy as np
import matplotlib.pyplot as plt
plt.style.use("ggplot")

S = 12
N = 1000
X_max = []
for i in range(N):
    samples = np.random.uniform(0, 1, S)
    X_max.append(max(samples))

# Plot the sample distirbution
plt.hist(X_max)
plt.show()
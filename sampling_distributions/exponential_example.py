import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
plt.style.use('ggplot')

def f(x, lam):
    """ pdf for exponential distribution with lam=1/15 """
    return (lam) * np.e ** (-x * lam)

lam = 1 / 15
x = np.linspace(0, 100, 1000)
pdf_x = f(x, lam)

# Plot the pdf
plt.plot(x, pdf_x)
plt.show()

N = 1000
S = 100
X_bar = []
for i in range(N):
    # numpy scale is 1/param
    samples = np.random.exponential(1/lam, S)
    X_bar.append(np.mean(samples))
    
print(f"Mean X_bar: {np.mean(X_bar)}")
print(f"SD X_bar:   {np.std(X_bar)}")

# Sample distribution
plt.hist(X_bar)
plt.show()

# QQ Plot of sample distirbution
sm.qqplot(np.array(X_bar))
plt.show()
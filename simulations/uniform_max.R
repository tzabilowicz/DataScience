# Simulate sampling distribution of scaled max for uniform data
# In practice, we dont know theta. We substitute the actual value of T
# for theta T=((n+1)/n) * max(unif[0,theta])

n = 12
theta = 1 # unknown to us

B = 5000
T.scaled = numeric(B)

set.seed(381)

# Compute max of the Uniform random samples
for (b in 1:B) {
  # Scale the max
  T.scaled[b] = ((n+1)/n) * max(runif(n=n, max=theta))
}

hist(T.scaled, col="lightblue", main="Scaled Max of Uniform Data", freq=FALSE)
abline(v=theta, lty="dashed", col="red")
mean(T.scaled)

# Plot derived pdf
t.dummy = seq(0, max(T.scaled), length.out=500)
lines(x=t.dummy, y=n^(n+1)*t.dummy^(n-1)/((n+1)*theta)^n, col="blue")

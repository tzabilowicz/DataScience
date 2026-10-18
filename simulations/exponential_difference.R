l.X = 1/15 # Lambda for X
l.Y = 1/16 # Lambda for Y

n.X = n.Y = 100

# Simulate once by randomly sampling distributions
set.seed(381)

X = rexp(n=n.X, rate=l.X)
Y = rexp(n=n.Y, rate=l.Y)

# Plot random samples (density scale) and pdfs
big.val = max(c(X, Y))
dummy.vec = seq(0, big.val, length.out=500)

par(mfrow=c(1, 2))
hist(X, main="Exponential (X)", xlab="X", xlim=c(0, big.val), freq=FALSE, col="lightblue")
lines(x=dummy.vec, y=dexp(x=dummy.vec, rate=l.X))
hist(Y, main="Exponential (Y)", xlab="Y", xlim=c(0, big.val), freq=FALSE, col="lightblue")
lines(x=dummy.vec, y=dexp(x=dummy.vec, rate=l.Y))

# What will the distribution of T = Y_bar - X_bar look like?
N = 5000
T = numeric(N)
set.seed(381)

for (i in 1:N) {
  X = rexp(n=n.X, rate=l.X)
  Y = rexp(n=n.Y, rate=l.Y)
  T[i] = mean(Y) - mean(X)
}

par(mfrow=c(1,1))
hist(T, main="Difference of Means (Y-X", xlab="Y_bar-X_bar", col="lightgreen", freq=FALSE)

# Compute mean and standard error of T
T.mu = (1/l.Y) - (1/l.X)
T.se = sqrt((1/(n.Y*l.Y^2)) + (1/(n.X*l.X^2)))

# Add statistics to the plot
abline(v=T.mu, col="red")
arrows(x0=T.mu-T.se, x1=T.mu+T.se, y0=0.15, col="blue",
       lty="dashed", code=3, angle=90, length=0.2)

cat("T Mean: ", T.mu, "\n", sep="")
cat("T SE:   ", T.se, "\n", sep="")

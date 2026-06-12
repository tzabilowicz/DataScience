# Read Phillies data
phillies = read.csv("E:\\DataScience\\Data\\Phillies2009.csv")

summary(phillies)

# Compare empirical distributions for number of strikeouts
# per game, home and away.
home_strikeouts = phillies[phillies$Location == "Home", "StrikeOuts"]
away_strikeouts = phillies[phillies$Location == "Away", "StrikeOuts"]
  
plot.ecdf(home_strikeouts, xlab="Strike Outs", col="blue", main="Empirical CDF of Strike Outs: Home vs Away")
plot.ecdf(away_strikeouts, col="red", add=TRUE)
legend("topleft", legend=c("Home", "Away"), col=c("blue","red"))

# Mean strike outs home and away
M_SH = mean(home_strikeouts)
M_SA = mean(away_strikeouts)

print(M_SH)
print(M_SA)

# Permutation Test: Strike Outs
# Let M_SA = Mean number of strike outs at away games
# Let M_SH = Mean number of strike outs at home games
# The test statistic:
#   T = M_SH - M_SA
# 
# H0: M_SH - M_SA = 0
# HA: M_SH - M_SA != 0

t_obs = M_SH - M_SA
t_obs

T = 10000
N = length(home_strikeouts)
pooled = phillies$StrikeOuts

t_sample = numeric(T)
for (i in 1:T) {
  index = sample(length(pooled), N, replace=FALSE)
  t_sample[i] = mean(pooled[index]) - mean(pooled[-index])
}

# Compute the p-value (two-sided)
p_value = (sum(abs(t_sample) >= abs(t_obs)) + 1) / (length(t_sample) + 1) * 2
p_value

# Plot the test statistic distribution
hist(t_sample, col="skyblue", main="Sample Test Statistics")
abline(v=t_obs, col="red", lty="dashed")
# Read Phillies data
phillies = read.csv("E:\\DataScience\\Data\\Phillies2009.csv")

summary(phillies)

# Extract home and away data
home = phillies[phillies$Location == "Home",]
away = phillies[phillies$Location == "Away",]

# Permutation test parameters
T = 10000

# Permutation Test: Strike Outs ==============================
# Let M_SA = Mean number of strike outs at away games
# Let M_SH = Mean number of strike outs at home games
# The test statistic:
#   T = M_SH - M_SA
#
# H0: M_SH - M_SA = 0
# HA: M_SH - M_SA != 0

home_strikeouts = home$StrikeOuts
away_strikeouts = away$StrikeOuts

# Compare empirical distributions for number of strikeouts
# per game, home and away.
plot.ecdf(home_strikeouts, xlab="Strike Outs", col="blue", main="Empirical CDF of Strike Outs: Home vs Away")
plot.ecdf(away_strikeouts, col="red", add=TRUE)
legend("topleft", legend=c("Home", "Away"), col=c("blue","red"))

# Mean strike outs home and away
M_SH = mean(home_strikeouts)
M_SA = mean(away_strikeouts)

print(M_SH)
print(M_SA)

t_obs = M_SH - M_SA
t_obs

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

# Permutation Test: Home Runs ==============================
# Let M_RA = Mean number of home runs at away games
# Let M_RH = Mean number of home runs at home games
# The test statistic:
#   T = M_RH - M_RA
#
# H0: M_RH - M_RA = 0
# HA: M_RH - M_RA != 0

home_homeruns = home$Homeruns
away_homeruns = away$Homeruns

# Compare empirical distributions for number of homeruns
# per game, home and away.
plot.ecdf(home_homeruns, xlab="Homeruns", col="blue", main="Empirical CDF of Homeruns: Home vs Away")
plot.ecdf(away_homeruns, col="red", add=TRUE)
legend("topleft", legend=c("Home", "Away"), col=c("blue","red"))

# Mean homeruns home and away
M_RH = mean(home_homeruns)
M_RA = mean(away_homeruns)

t_obs = M_RH - M_RA
t_obs

N = length(home_homeruns)
pooled = phillies$Homeruns

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
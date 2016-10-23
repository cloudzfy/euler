# In England the currency is made up of pound, and pence, p, and
# there are eight coins in general circulation:

# 1p, 2p, 5p, 10p, 20p, 50p, 100p and 200p.
# It is possible to make 200p in the following way:

# 1x100p + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p
# How many different ways can 200p be made using any number of coins?

dp = [0 for x in range(201)]
dp[0] = 1
coins = [1, 2, 5, 10, 20, 50, 100, 200]

for c in coins:
	for i in range(c, len(dp)):
		dp[i] += dp[i - c]

print dp[-1]

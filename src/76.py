# It is possible to write five as a sum in exactly six
# different ways:

# 4 + 1
# 3 + 2
# 3 + 1 + 1
# 2 + 2 + 1
# 2 + 1 + 1 + 1
# 1 + 1 + 1 + 1 + 1

# How many different ways can one hundred be written as
# a sum of at least two positive integers?

dp = [0 for i in range(101)]
dp[0] = 1

for x in range(1, 100):
	for i in range(x, len(dp)):
		dp[i] += dp[i - x]

print dp[-1]

# Let p(n) represent the number of different ways in whichn coins can
# be separated into piles. For example, five coins can be separated
# into piles in exactly seven different ways, so p(5) = 7.

# OOOOO
# OOOO O
# OOO OO
# OOO O O
# OO OO O
# OO O O O
# O O O O O

# Find the least value of n for which p(n) is divisible by one million.

n = 10000

dp = [0 for i in range(n + 1)]
dp[0] = 1
for x in range(1, n + 1):
	for i in range(x, len(dp)):
		dp[i] += dp[i - x]

for i in range(len(dp)):
	if dp[i] % 1000000 == 0:
		print i
		break

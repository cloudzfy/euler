# Starting in the top left corner of a 2x2 grid, and only being able to move to
# the right and down, there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20x20 grid?

size = 21

dp = [[0 for i in range(size)] for j in range(size)]

dp[0][0] = 1

for i in range(1, size):
	dp[i][0] = 1
	dp[0][i] = 1

for i in range(1, size):
	for j in range(1, size):
		dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

print dp[size - 1][size - 1]
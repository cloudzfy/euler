# In the 5 by 5 matrix below, the minimal path sum from
# the top left to the bottom right, by only moving to the
# right and down, is indicated in bold red and is equal
# to 2427.

# 131 673 234 103 18
# 201 96  342 965 150
# 630 803 746 422 111
# 537 699 497 121 956
# 805 732 524 37  331

# Find the minimal path sum, in matrix.txt (right click
# and "Save Link/Target As..."), a 31K text file containing
# a 80 by 80 matrix, from the top left to the bottom right
# by only moving right and down.

from copy import copy

file = open('../data/p081_matrix.txt', 'r')
data = file.read()
file.close()

matrix = [[int(x) for x in l.split(',')] for l in data.split('\n')[:-1]]

limit = sum([sum(l) for l in matrix])

n = len(matrix)
m = len(matrix[0])
dp = [[limit for x in range(m)] for y in range(n)]
dp[0][0] = matrix[0][0]

for x in range(n):
	for y in range(m):
		if x <> 0:
			dp[x][y] = min(dp[x][y], matrix[x][y] + dp[x - 1][y])
		if y <> 0:
			dp[x][y] = min(dp[x][y], matrix[x][y] + dp[x][y - 1])

print dp[n - 1][m - 1]

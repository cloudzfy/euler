# The minimal path sum in the 5 by 5 matrix below, by starting
# in any cell in the left column and finishing in any cell in
# the right column, and only moving up, down, and right, is
# indicated in red and bold; the sum is equal to 994.

# 131 673 234 103 18
# 201 96  342 965 150
# 630 803 746 422 111
# 537 699 497 121 956
# 805 732 524 37  331

# Find the minimal path sum, in matrix.txt (right click and
# "Save Link/Target As..."), a 31K text file containing a 80
# by 80 matrix, from the left column to the right column.

file = open('../data/p082_matrix.txt', 'r')
data = file.read()
file.close()

matrix = [[int(x) for x in l.split(',')] for l in data.split('\n')[:-1]]
limit = sum([sum(l) for l in matrix])

n = len(matrix)
m = len(matrix[0])
dp = [[limit for x in range(m)] for y in range(n)]

for y in range(m):
	if y == 0:
		for x in range(n):
			dp[x][y] = matrix[x][y]
	else:
		for x in range(n):
			dp[x][y] = matrix[x][y] + dp[x][y - 1]
			if x <> 0:
				dp[x][y] = min(dp[x][y], dp[x - 1][y] + matrix[x][y])
		for x in range(n - 2, -1, -1):
			dp[x][y] = min(dp[x][y], dp[x + 1][y] + matrix[x][y])

print min([l[-1] for l in dp])

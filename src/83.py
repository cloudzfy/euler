# In the 5 by 5 matrix below, the minimal path sum from the top
# left to the bottom right, by moving left, right, up, and down,
# is indicated in bold red and is equal to 2297.

# 131 673 234 103 18
# 201 96  342 965 150
# 630 803 746 422 111
# 537 699 497 121 956
# 805 732 524 37  331

# Find the minimal path sum, in matrix.txt (right click and
# "Save Link/Target As..."), a 31K text file containing a 80 by
# 80 matrix, from the top left to the bottom right by moving
# left, right, up, and down.

from Queue import PriorityQueue

file = open('../data/p083_matrix.txt', 'r')
data = file.read()
file.close()

matrix = [[int(x) for x in l.split(',')] for l in data.split('\n')[:-1]]
limit = sum([sum(l) for l in matrix]) + 1

n = len(matrix)
m = len(matrix[0])
dp = [[limit for x in range(m)] for y in range(n)]
visited = [[False for x in range(m)] for y in range(n)]
queue = PriorityQueue()

queue.put((matrix[0][0], 0, 0))
steps = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def check_boundary(x, y):
	return x >= 0 and x < n and y >= 0 and y < m

while not queue.empty():
	(cur, x, y) = queue.get()
	dp[x][y] = min(dp[x][y], cur)
	if visited[x][y]:
		continue
	visited[x][y] = True
	for s in steps:
		_x, _y = x + s[0], y + s[1]
		if check_boundary(_x, _y) and not visited[_x][_y]:
			queue.put((cur + matrix[_x][_y], _x, _y))

print dp[n - 1][m - 1]

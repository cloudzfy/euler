# The following undirected network consists of seven vertices and twelve
# edges with a total weight of 243.

# [../img/p107_1.gif]

# The same network can be represented by the matrix below.

#         A   B   C   D   E   F   G
#     A   -   16  12  21  -   -   -
#     B   16  -   -   17  20  -   -
#     C   12  -   -   28  -   31  -
#     D   21  17  28  -   18  19  23
#     E   -   20  -   18  -   -   11
#     F   -   -   31  19  -   -   27
#     G   -   -   -   23  11  27  -

# However, it is possible to optimise the network by removing some edges
# and still ensure that all points on the network remain connected. The
# network which achieves the maximum saving is shown below. It has a
# weight of 93, representing a saving of 243 - 93 = 150 from the original
# network.

# [../img/p107_2.gif]

# Using network.txt (right click and 'Save Link/Target As...'), a 6K text
# file containing a network with forty vertices, and given in matrix form,
# find the maximum saving which can be achieved by removing redundant edges
# whilst ensuring that the network remains connected.

from Queue import PriorityQueue

file = open('../data/p107_network.txt', 'r')
data = file.read()
file.close()

matrix = [line.split(',') for line in data.split('\n')[:-1]]
queue = PriorityQueue()
total = 0
n = len(matrix)
for i in range(n):
	for j in range(i):
		if matrix[i][j] <> '-':
			queue.put((int(matrix[i][j]), i, j))
			total += int(matrix[i][j])

pre = range(n)

def find(x):
	if pre[x] <> x:
		pre[x] = find(pre[x])
	return pre[x]

def merge(x, y):
	x = find(x)
	y = find(y)
	if x <> y:
		pre[x] = y

count = 0
ans = 0

while count < n - 1:
	(val, x, y) = queue.get()
	if find(x) <> find(y):
		merge(x, y)
		ans += val
		count += 1

print total - ans

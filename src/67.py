# By starting at the top of the triangle below and moving to adjacent
# numbers on the row below, the maximum total from top to bottom is 23.

#    3
#   7 4
#  2 4 6
# 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom in triangle.txt (right click
# and 'Save Link/Target As...'), a 15K text file containing a triangle
# with one-hundred rows.

# NOTE: This is a much more difficult version of Problem 18. It is not
# possible to try every route to solve this problem, as there are 299
# altogether! If you could check one trillion (1012) routes every second
# it would take over twenty billion years to check them all. There is an
# efficient algorithm to solve it. ;o)

file = open('../data/p067_triangle.txt', 'r')
data = file.read()
file.close()

nums = [[int(x) for x in line.split(' ')] for line in data.split('\n')[:-1]]
for i in range(1, len(nums)):
	nums[i][0] += nums[i - 1][0]
	for j in range(1, len(nums[i - 1])):
		nums[i][j] += max(nums[i - 1][j - 1], nums[i - 1][j])
	nums[i][-1] += nums[i - 1][-1]

print max(nums[-1])

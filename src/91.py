# The points P (x_1, y_1) and Q (x_2, y_2) are plotted at
# integer co-ordinates and are joined to the origin, O(0,0),
# to form OPQ.

# [../img/p091_1.gif]

# There are exactly fourteen triangles containing a right
# angle that can be formed when each co-ordinate lies between
# 0 and 2 inclusive; that is,

# 0 <= x_1, y_1, x_2, y_2 <= 2.

# [../img/p091_2.gif]

# Given that 0 <= x_1, y_1, x_2, y_2 <= 50, how many right
# triangles can be formed?

from fractions import gcd

limit = 50
count = 0

for x in range(1, limit + 1):
	for y in range(1, limit + 1):
		d = gcd(x, y)
		count += min((limit - x) * d / y, y * d / x)

print count * 2 + limit * limit * 3

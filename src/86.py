# A spider, S, sits in one corner of a cuboid room, measuring
# 6 by 5 by 3, and a fly, F, sits in the opposite corner. By
# travelling on the surfaces of the room the shortest "straight
# line" distance from S to F is 10 and the path is shown on the
# diagram.

# [../img/p086.gif]

# However, there are up to three "shortest" path candidates for
# any given cuboid and the shortest route doesn't always have
# integer length.

# It can be shown that there are exactly 2060 distinct cuboids,
# ignoring rotations, with integer dimensions, up to a maximum
# size of M by M by M, for which the shortest route has integer
# length when M = 100. This is the least value of M for which
# the number of solutions first exceeds two thousand; the number
# of solutions when M = 99 is 1975.

# Find the least value of M such that the number of solutions
# first exceeds one million.

from math import sqrt

M = 0
limit = 1000000
count = 0

while count <= limit:
	M += 1
	for L in range(2, M * 2 + 1):
		tmp = sqrt(M * M + L * L)
		if tmp == int(tmp):
			count += L / 2 if L <= M else M - (L - 1) / 2

print M

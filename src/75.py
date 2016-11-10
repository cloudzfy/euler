# It turns out that 12 cm is the smallest length of wire that can be
# bent to form an integer sided right angle triangle in exactly one
# way, but there are many more examples.

# 12 cm: (3,4,5)
# 24 cm: (6,8,10)
# 30 cm: (5,12,13)
# 36 cm: (9,12,15)
# 40 cm: (8,15,17)
# 48 cm: (12,16,20)

# In contrast, some lengths of wire, like 20 cm, cannot be bent to
# form an integer sided right angle triangle, and other lengths allow
# more than one solution to be found; for example, using 120 cm it is
# possible to form exactly three different integer sided right angle
# triangles.

# 120 cm: (30,40,50), (20,48,52), (24,45,51)

# Given that L is the length of the wire, for how many values of
# L <= 1,500,000 can exactly one integer sided right angle triangle
# be formed?

from math import sqrt
from fractions import gcd

L = {}
limit = 1500000
mlimit = int(sqrt(limit))

for m in range(2, mlimit):
	for n in range(1, m):
		if gcd(m, n) == 1 and (n + m) % 2 == 1:
			p = 2 * m * (m + n)
			tmp = p
			while tmp <= limit:
				if tmp in L:
					L[tmp] += 1
				else:
					L[tmp] = 1
				tmp += p

ans = 0

for k, v in L.items():
	if v == 1:
		ans += 1

print ans


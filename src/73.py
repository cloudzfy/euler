# Consider the fraction, n / d, where n and d are positive
# integers. If n < d and HCF(n,d) = 1, it is called a reduced
# proper fraction.

# If we list the set of reduced proper fractions for d <= 8
# in ascending order of size, we get:

# 1 / 8, 1 / 7, 1 / 6, 1 / 5, 1 / 4, 2 / 7, 1 / 3, 3 / 8,
# 2 / 5, 3 / 7, 1 / 2, 4 / 7, 3 / 5, 5 / 8, 2 / 3, 5 / 7,
# 3 / 4, 4 / 5, 5 / 6, 6 / 7, 7 / 8

# It can be seen that there are 3 fractions between 1 / 3
# and 1 / 2.

# How many fractions lie between 1 / 3 and 1 / 2 in the
# sorted set of reduced proper fractions for d <= 12,000?

from fractions import gcd
from math import ceil

def get_fractions(d):
	count = 0
	i = int(ceil(float(d) / 3))
	while 2 * i < d:
		if gcd(i, d) == 1:
			count += 1
		i += 1
	return count

print sum([get_fractions(d) for d in range(4, 12001)])

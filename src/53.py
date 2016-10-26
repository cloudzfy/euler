# There are exactly ten ways of selecting three from five, 12345:

# 123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

# In combinatorics, we use the notation, 5C3 = 10.

# In general,

# nCr = n!/(r!(n - r)!),where r <= n, n! = n x (n - 1) x ... x 3 x 2 x 1,
# and 0! = 1.

# It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

# How many, not necessarily distinct, values of  nCr, for 1 <= n <= 100, are
# greater than one-million?

from math import factorial

fact = [factorial(x) for x in range(101)]

def get_combination(n, r):
	return fact[n] / fact[r] / fact[n - r]

count = 0
for n in range(1, 101):
	for r in range(0, n + 1):
		if get_combination(n, r) > 1000000:
			count += 1

print count

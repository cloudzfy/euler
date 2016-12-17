# Working from left-to-right if no digit is exceeded by the digit to its
# left it is called an increasing number; for example, 134468.

# Similarly if no digit is exceeded by the digit to its right it is called
# a decreasing number; for example, 66420.

# We shall call a positive integer that is neither increasing nor decreasing
# a "bouncy" number; for example, 155349.

# As n increases, the proportion of bouncy numbers below n increases such
# that there are only 12951 numbers below one-million that are not bouncy
# and only 277032 non-bouncy numbers below 10^10.

# How many numbers below a googol (10^100) are not bouncy?

from math import factorial

def combination(k, n):
	if k == 0 or k > n:
		return 1
	return reduce(lambda x, y: x * y, range(n - k + 1, n + 1)) / factorial(k)

inc = combination(9, 109) - 1
dec = combination(10, 110) - 1 - 100 * 10

print inc + dec

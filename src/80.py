# It is well known that if the square root of a natural number
# is not an integer, then it is irrational. The decimal expansion
# of such square roots is infinite without any repeating pattern
# at all.

# The square root of two is 1.41421356237309504880..., and the
# digital sum of the first one hundred decimal digits is 475.

# For the first one hundred natural numbers, find the total of
# the digital sums of the first one hundred decimal digits for
# all the irrational square roots.

from math import sqrt

limit = pow(10, 101)

def sum_of_decimal_digits(num):
	a = 5 * num
	b = 5
	while b < limit:
		if a >= b:
			a -= b
			b += 10
		else:
			a *= 100
			b = b / 10 * 100 + 5
	return sum([int(x) for x in str(b / 100)])

def has_irrational_root(num):
	x = int(sqrt(num))
	return x * x <> num

ans = 0
for i in range(1, 101):
	if has_irrational_root(i):
		ans += sum_of_decimal_digits(i)

print ans

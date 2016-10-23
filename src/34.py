# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

# Find the sum of all numbers which are equal to the sum of the
# factorial of their digits.

# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

from math import factorial

fact = [factorial(x) for x in range(0, 10)]

def is_factorial_sum(num):
	ret = 0
	for x in list(str(num)):
		ret += fact[int(x)]
	return ret == num

ans = 0

for i in range(10, 2550000):
	if is_factorial_sum(i):
		ans += i

print ans

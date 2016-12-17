# In the following equation x, y, and n are positive integers.

#     1   1   1
#     - + - = -
#     x   y   n

# For n = 4 there are exactly three distinct solutions:

#     1    1   1
#     - + -- = -
#     5   20   4

#     1    1   1
#     - + -- = -
#     6   12   4

#     1   1   1
#     - + - = -
#     8   8   4

# What is the least value of n for which the number of distinct
# solutions exceeds one-thousand?

# NOTE: This problem is an easier version of Problem 110; it is
# strongly advised that you solve this one first.

from math import sqrt

def generate_primes(limit):
	is_prime = [True for i in range(limit)]
	for i in range(2, int(sqrt(limit))):
		if is_prime[i]:
			for j in range(i * i, limit, i):
				is_prime[j] = False
	return filter(lambda x: is_prime[x], range(2, limit))

primes = generate_primes(18)

def count_divisors(num):
	count = 1
	for p in primes:
		if num % p == 0:
			tmp = 0
			while num % p == 0:
				num /= p
				tmp += 1
			count *= tmp * 2 + 1
		if num == 1:
			break
	return count

ans = 1
while True:
	if (count_divisors(ans) + 1) / 2 > 1000:
		break
	ans += 1

print ans

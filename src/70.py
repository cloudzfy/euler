# Euler's Totient function, phi(n) [sometimes called the phi function],
# is used to determine the number of positive numbers less than or
# equal to n which are relatively prime to n. For example, as 1, 2,
# 4, 5, 7, and 8, are all less than nine and relatively prime to
# nine, phi(9) = 6.

# The number 1 is considered to be relatively prime to every positive
# number, so phi(1) = 1.

# Interestingly, phi(87109) = 79180, and it can be seen that 87109 is
# a permutation of 79180.

# Find the value of n, 1 < n < 107, for which phi(n) is a permutation
# of n and the ratio n / phi(n) produces a minimum.

from math import sqrt

def generate_primes(limit):
	is_prime = [True for i in range(limit)]
	for i in range(2, int(sqrt(limit))):
		if is_prime[i]:
			for j in range(i * i, limit, i):
				is_prime[j] = False
	return filter(lambda x: is_prime[x], range(2, limit))

primes = generate_primes(5000)

def is_permutation(x, y):
	return sorted(str(x)) == sorted(str(y))

ans = 0
val = 10000

for a in primes:
	for b in primes:
		n = a * b
		if n > 10000000:
			continue
		phi = (a - 1) * (b - 1)
		if is_permutation(n, phi):
			if float(n) / phi < val:
				ans, val = n, float(n) / phi

print ans


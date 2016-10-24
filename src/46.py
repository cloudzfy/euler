# It was proposed by Christian Goldbach that every odd composite number
# can be written as the sum of a prime and twice a square.

# 9 = 7 + 2x12
# 15 = 7 + 2x22
# 21 = 3 + 2x32
# 25 = 7 + 2x32
# 27 = 19 + 2x22
# 33 = 31 + 2x12

# It turns out that the conjecture was false.

# What is the smallest odd composite that cannot be written as the sum of
# a prime and twice a square?

from math import sqrt

def generate_primes(limit):
	isPrime = [True for i in range(limit)]
	for i in range(2, int(sqrt(limit))):
		if isPrime[i]:
			for j in range(i * i, limit, i):
				isPrime[j] = False
	return filter(lambda x: isPrime[x], range(2, limit))

primes = set(generate_primes(10000))

for i in range(9, 10000, 2):
	isFound = False
	if i not in primes:
		for j in range(1, int(sqrt(i / 2)) + 1):
			if i - 2 * j * j in primes:
				isFound = True
		if not isFound:
			print i
			break
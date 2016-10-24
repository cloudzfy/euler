# The prime 41, can be written as the sum of six consecutive primes:

# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime
# below one-hundred.

# The longest sum of consecutive primes below one-thousand that adds
# to a prime, contains 21 terms, and is equal to 953.

# Which prime, below one-million, can be written as the sum of the
# most consecutive primes?

from math import sqrt
from copy import copy

def generate_primes(limit):
	isPrime = [True for i in range(limit)]
	for i in range(2, int(sqrt(limit))):
		if isPrime[i]:
			for j in range(i * i, limit, i):
				isPrime[j] = False
	return filter(lambda x: isPrime[x], range(2, limit))

primes = generate_primes(1000000)
prime_set = set(primes)

prime_sum = copy(primes)
for i in range(1, len(primes)):
	prime_sum[i] += prime_sum[i - 1]

prime_sum.insert(0, 0)

ans = 0
left = 21
right = len(primes) + 1
for i in range(len(primes)):
	for j in range(i + left, right):
		p = prime_sum[j] - prime_sum[i]
		if p > 1000000:
			right = j
			break
		if p in prime_set:
			if left < j - i:
				ans, left = p, j - i
print ans

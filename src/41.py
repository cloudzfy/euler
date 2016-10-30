# We shall say that an n-digit number is pandigital if it makes use of
# all the digits 1 to n exactly once. For example, 2143 is a 4-digit
# pandigital and is also prime.

# What is the largest n-digit pandigital prime that exists?

from math import sqrt

def generate_primes(limit):
	is_prime = [True for i in range(limit)]
	for i in range(2, int(sqrt(limit))):
		if is_prime[i]:
			for j in range(i * i, limit, i):
				is_prime[j] = False
	return filter(lambda x: is_prime[x], range(2, limit))

primes = generate_primes(7654321)

def is_pandigital(num):
	a = ''.join(sorted(str(num)))
	b = ''.join([str(x) for x in range(1, len(str(num)) + 1)])
	return a == b

ans = 0
for p in primes:
	if is_pandigital(p):
		ans = p

print ans

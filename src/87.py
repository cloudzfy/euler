# The smallest number expressible as the sum of a prime
# square, prime cube, and prime fourth power is 28. In
# fact, there are exactly four numbers below fifty that
# can be expressed in such a way:

# 28 = 2^2 + 2^3 + 2^4
# 33 = 3^2 + 2^3 + 2^4
# 49 = 5^2 + 2^3 + 2^4
# 47 = 2^2 + 3^3 + 2^4

# How many numbers below fifty million can be expressed
# as the sum of a prime square, prime cube, and prime
# fourth power?

from math import sqrt

def generate_primes(limit):
	is_prime = [True for i in range(limit)]
	for i in range(2, int(sqrt(limit))):
		if is_prime[i]:
			for j in range(i * i, limit, i):
				is_prime[j] = False
	return filter(lambda x: is_prime[x], range(2, limit))

limit = 50000000
primes = generate_primes(int(sqrt(limit)) + 1)
powers = [(pow(x, 2), pow(x, 3), pow(x, 4)) for x in primes]

ans = set()

for a in powers:
	for b in powers:
		for c in powers:
			tmp = a[0] + b[1] + c[2]
			if tmp < limit:
				ans.add(tmp)
			else:
				break

print len(ans)

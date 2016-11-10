# It is possible to write ten as the sum of primes in exactly
# five different ways:

# 7 + 3
# 5 + 5
# 5 + 3 + 2
# 3 + 3 + 2 + 2
# 2 + 2 + 2 + 2 + 2

# What is the first value which can be written as the sum of
# primes in over five thousand different ways?

from math import sqrt

def generate_primes(limit):
	is_prime = [True for i in range(limit)]
	for i in range(2, int(sqrt(limit))):
		if is_prime[i]:
			for j in range(i * i, limit, i):
				is_prime[j] = False
	return filter(lambda x: is_prime[x], range(2, limit))

val = 100
primes = generate_primes(val)

dp = [0 for i in range(val + 1)]
dp[0] = 1

for p in primes:
	for i in range(p, len(dp)):
		dp[i] += dp[i - p]

for i in range(len(dp)):
	if dp[i] > 5000:
		print i
		break

# Euler's Totient function, phi(n) [sometimes called the phi function],
# is used to determine the number of numbers less than n which are
# relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all
# less than nine and relatively prime to nine, phi(9) = 6.

# n     Relatively Prime     phi(n)     n/phi(n)
# 2     1                    1          2
# 3     1,2                  2          1.5
# 4     1,3                  2          2
# 5     1,2,3,4              4          1.25
# 6     1,5                  2          3
# 7     1,2,3,4,5,6          6          1.1666...
# 8     1,3,5,7              4          2
# 9     1,2,4,5,7,8          6          1.5
# 10    1,3,7,9              4          2.5

# It can be seen that n = 6 produces a maximum n / phi(n) for n <= 10.

# Find the value of n <= 1,000,000 for which n / phi(n) is a maximum.

from math import sqrt

def generate_primes(limit):
	is_prime = [True for i in range(limit)]
	for i in range(2, int(sqrt(limit))):
		if is_prime[i]:
			for j in range(i * i, limit, i):
				is_prime[j] = False
	return filter(lambda x: is_prime[x], range(2, limit))

primes = generate_primes(1000)

ans = 1

for p in primes:
	if ans * p > 1000000:
		break
	ans *= p

print ans

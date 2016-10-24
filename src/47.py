# The first two consecutive numbers to have two distinct prime
# factors are:

# 14 = 2 x 7
# 15 = 3 x 5

# The first three consecutive numbers to have three distinct
# prime factors are:

# 644 = 2^2 x 7 x 23
# 645 = 3 x 5 x 43
# 646 = 2 x 17 x 19.

# Find the first four consecutive integers to have four distinct
# prime factors. What is the first of these numbers?

from math import sqrt

def generate_primes(limit):
	isPrime = [True for i in range(limit)]
	for i in range(2, int(sqrt(limit))):
		if isPrime[i]:
			for j in range(i * i, limit, i):
				isPrime[j] = False
	return filter(lambda x: isPrime[x], range(2, limit))

primes = generate_primes(400)

def count_prime_factors(num):
	count = 0
	for p in primes:
		if p * p > num:
			count += 1
			break
		hasFactor = False
		while num % p == 0:
			num /= p
			hasFactor = True
		if hasFactor:
			count += 1
		if num == 1:
			break
	return count

nums = []
num = 644
while len(nums) < 4:
	if count_prime_factors(num) >= 4:
		nums.append(num)
	else:
		nums = []
	num += 1

print nums[0]

# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
# increases by 3330, is unusual in two ways: (i) each of the three terms
# are prime, and, (ii) each of the 4-digit numbers are permutations of
# one another.

# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit
# primes, exhibiting this property, but there is one other 4-digit
# increasing sequence.

# What 12-digit number do you form by concatenating the three terms in
# this sequence?

from math import sqrt
from itertools import permutations

def generate_primes(limit):
	is_prime = [True for i in range(limit)]
	for i in range(2, int(sqrt(limit))):
		if is_prime[i]:
			for j in range(i * i, limit, i):
				is_prime[j] = False
	return filter(lambda x: is_prime[x], range(1000, limit))

primes = set(generate_primes(9999))

ans = []
for p in primes:
	if p == 1487:
		continue
	nums = []
	for x in permutations(str(p)):
		tmp = int(''.join(x))
		if tmp in primes:
			nums.append(tmp)
	if len(nums) > 2:
		for x in nums:
			if x > p and 2 * x - p in nums:
				print str(p) + str(x) + str(2 * x - p)
				break

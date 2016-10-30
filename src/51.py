# By replacing the 1st digit of the 2-digit number *3, it turns out
# that six of the nine possible values: 13, 23, 43, 53, 73, and 83,
# are all prime.

# By replacing the 3rd and 4th digits of 56**3 with the same digit,
# this 5-digit number is the first example having seven primes among
# the ten generated numbers, yielding the family: 56003, 56113, 56333,
# 56443, 56663, 56773, and 56993. Consequently 56003, being the first
# member of this family, is the smallest prime with this property.

# Find the smallest prime which, by replacing part of the number (not
# necessarily adjacent digits) with the same digit, is part of an
# eight prime value family.

from math import sqrt
from itertools import product

def generate_primes(limit):
	is_prime = [True for i in range(limit)]
	for i in range(2, int(sqrt(limit))):
		if is_prime[i]:
			for j in range(i * i, limit, i):
				is_prime[j] = False
	return filter(lambda x: is_prime[x], range(2, limit))

primes = set(generate_primes(1000000))

def count_prime_w_replacement(num, digit):
	count = 0
	for c in range(0, 10):
		tmp = num.replace(digit, str(c))
		if tmp[0] <> '0' and int(tmp) in primes:
			count += 1
	return count

ans = 1000000
for p in primes:
	num = str(p)
	for c in range(0, 3):
		if num.count(str(c)) == 3 and count_prime_w_replacement(num, str(c)) > 7:
			ans = min(ans, p)

print ans

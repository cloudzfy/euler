# The primes 3, 7, 109, and 673, are quite remarkable. By taking
# any two primes and concatenating them in any order the result
# will always be prime. For example, taking 7 and 109, both 7109
# and 1097 are prime. The sum of these four primes, 792, represents
# the lowest sum for a set of four primes with this property.

# Find the lowest sum for a set of five primes for which any two
# primes concatenate to produce another prime.

from math import sqrt
from random import randrange

def is_prime_miller_rabin(num):
	if num == 2:
		return True
	if num % 2 == 0:
		return False
	d = num - 1
	r = 0
	while d % 2 == 0:
		d /= 2
		r += 1
	for i in range(20):
		a = randrange(2, num, 1)
		x = pow(a, d, num)
		if x == 1 or x == num - 1:
			continue
		isComposite = True
		for j in range(r - 1):
			x = x * x % num
			if x == 1:
				return False
			if x == num - 1:
				isComposite = False
				break
		if isComposite:
			return False
	return True

def generate_primes(limit):
	is_prime = [True for i in range(limit)]
	for i in range(2, int(sqrt(limit))):
		if is_prime[i]:
			for j in range(i * i, limit, i):
				is_prime[j] = False
	return filter(lambda x: is_prime[x], range(2, limit))

primes = generate_primes(10000)

def check_concatenation_primality(nums, p):
	for c in nums:
		if not is_prime_miller_rabin(int(str(c) + str(p))):
			return False
		if not is_prime_miller_rabin(int(str(p) + str(c))):
			return False
	return True

def get_valid_primes(nums, myprimes):
	ret = []
	for p in myprimes:
		if check_concatenation_primality(nums, p):
			ret.append(p)
	return ret

ans = 10000000

def solve():
	for a in primes:
		myprimes_a = get_valid_primes([a], primes)
		for b in myprimes_a:
			myprimes_b = get_valid_primes([a, b], myprimes_a)
			for c in myprimes_b:
				myprimes_c = get_valid_primes([a, b, c], myprimes_b)
				for d in myprimes_c:
					myprimes_d = get_valid_primes([a, b, c, d], myprimes_c)
					for e in myprimes_d:
						return a + b + c + d + e

print solve()

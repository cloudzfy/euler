# The number 3797 has an interesting property. Being prime itself,
# it is possible to continuously remove digits from left to right,
# and remain prime at each stage: 3797, 797, 97, and 7. Similarly
# we can work from right to left: 3797, 379, 37, and 3.

# Find the sum of the only eleven primes that are both truncatable
# from left to right and right to left.

# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

def generate_primes(limit):
	isPrime = [True for i in range(limit)]
	for i in range(2, limit):
		if isPrime[i]:
			j = 2
			while i * j < limit:
				isPrime[i * j] = False
				j += 1
	return filter(lambda x: isPrime[x], range(2, limit))

primes = set(generate_primes(1000000))

def is_truncatable_prime(num):
	digits = list(str(num))
	if len(digits) == 1:
		return False
	while len(digits) > 1:
		digits.pop(0)
		if int(''.join(digits)) not in primes:
			return False
	digits = list(str(num))
	while len(digits) > 1:
		digits.pop()
		if int(''.join(digits)) not in primes:
			return False
	return True

ans = []

for p in primes:
	if is_truncatable_prime(p):
		ans.append(p)

print sum(ans)

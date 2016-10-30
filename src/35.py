# The number, 197, is called a circular prime because all rotations
# of the digits: 197, 971, and 719, are themselves prime.

# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17,
# 31, 37, 71, 73, 79, and 97.

# How many circular primes are there below one million?

def generate_primes(limit):
	is_prime = [True for i in range(limit)]
	for i in range(2, limit):
		if is_prime[i]:
			j = 2
			while i * j < limit:
				is_prime[i * j] = False
				j += 1
	return filter(lambda x: is_prime[x], range(2, limit))

primes = set(generate_primes(1000000))

ans = set()
def is_circular_prime(num):
	digits = list(str(num))
	for i in range(len(str(num)) - 1):
		digits.append(digits.pop(0))
		if int(''.join(digits)) not in primes:
			return False
	return True

def get_circular_primes(num):
	yield num
	digits = list(str(num))
	for i in range(len(str(num)) - 1):
		digits.append(digits.pop(0))
		yield int(''.join(digits))

for p in primes:
	if is_circular_prime(p) and p not in ans:
		[ans.add(x) for x in get_circular_primes(p)]

print len(ans)
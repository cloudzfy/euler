# Euler discovered the remarkable quadratic formula:

# n^2 + n + 41

# It turns out that the formula will produce 40 primes for the consecutive integer
# values 0 <= n <= 39. However, when n = 40, 40^2 + 40 + 41 = 40 (40 + 1) + 41 is
# divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible
# by 41.

# The incredible formula n^2 - 79n + 1601 was discovered, which produces 80 primes
# for the consecutive values 0 <= n <= 79. The product of the coefficients, -79
# and 1601, is -126479.

# Considering quadratics of the form: n^2 + an + b, where |a| < 1000 and |b| <= 1000
# where |n| is the modulus/absolute value of n
# e.g. |11| = 11 and |-4| = 4

# Find the product of the coefficients, a and b, for the quadratic expression that
# produces the maximum number of primes for consecutive values of n, starting with
# n = 0.

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
b_candidates = generate_primes(1000)

def count_produced_prime(a, b):
	ret = []
	for n in range(0, b):
		c = n * n + a * n + b
		if c in primes:
			ret.append(c)
		else:
			return len(ret)
	return len(ret)

ans = 0
count = 0
for b in b_candidates:
	for a in range(-999, 1000):
		tmp = count_produced_prime(a, b)
		if tmp > count:
			ans, count = a * b, tmp

print ans

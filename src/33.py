# The fraction 49/98 is a curious fraction, as an inexperiencedmathematician
# in attempting to simplify it may incorrectly believe that 49/98 = 4/8,
# which is correct, is obtained by cancelling the 9s.

# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

# There are exactly four non-trivial examples of this type of fraction,
# less than one in value, and containing two digits in the numerator and
# denominator.

# If the product of these four fractions is given in its lowest common 
# terms, find the value of the denominator.

numerator = 1
denominator = 1

def generate_primes(limit):
	is_prime = [True for i in range(limit)]
	for i in range(2, limit):
		if is_prime[i]:
			j = 2
			while i * j < limit:
				is_prime[i * j] = False
				j += 1
	return filter(lambda x: is_prime[x], range(2, limit))

primes = generate_primes(10000)

for a in range(1, 10):
	for b in range(1, 9):
		for c in range(b + 1, 10):
			if (10 * a + b) * c == (10 * c + a) * b or (10 * b + a) * c == (10 * a + c) * b:
				numerator *= b
				denominator *= c

for p in primes:
	while numerator % p == 0 and denominator % p == 0:
		numerator /= p
		denominator /= p

print denominator

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
# we can see that the 6th prime is 13.

# What is the 10 001st prime number?

size = 200000
is_prime = [True for i in range(size)]

for i in range(2, size):
	if is_prime[i]:
		j = 2
		while i * j < size:
			is_prime[i * j] = False
			j += 1

num = 1
for i in range(10001):
	num += 1
	while not is_prime[num]:
		num += 1

print num
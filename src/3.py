# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

from math import sqrt

num = 600851475143
size = int(sqrt(num)) + 1

is_prime = [True for i in range(size)]

for i in range(2, size):
	if is_prime[i]:
		j = 2
		while i * j < size:
			is_prime[i * j] = False
			j += 1

for i in range(size - 1, 1, -1):
	if is_prime[i] and num % i == 0:
		print i
		break

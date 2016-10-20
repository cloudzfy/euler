# The prime factors of 13195 are 5, 7, 13 and 29.
# 
# What is the largest prime factor of the number 600851475143 ?

from math import sqrt

num = 600851475143
size = int(sqrt(num)) + 1

isPrime = [True for i in range(size)]

for i in range(2, size):
	if isPrime[i]:
		j = 2
		while i * j < size:
			isPrime[i * j] = False
			j += 1

for i in range(size - 1, 1, -1):
	if isPrime[i] and num % i == 0:
		print i
		break

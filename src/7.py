# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
# we can see that the 6th prime is 13.
# 
# What is the 10 001st prime number?

size = 200000
isPrime = [True for i in range(size)]

for i in range(2, size):
	if isPrime[i]:
		j = 2
		while i * j < size:
			isPrime[i * j] = False
			j += 1

num = 1
for i in range(10001):
	num += 1
	while not isPrime[num]:
		num += 1

print num
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# 
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

size = 20
isPrime = [True for i in range(size)]

for i in range(2, size):
	if isPrime[i]:
		j = 2
		while i * j < size:
			isPrime[i * j] = False
			j += 1

countPrime = {}
for i in range(2, len(isPrime)):
	if isPrime[i]:
		countPrime[i] = 0

for i in range(2, 21):
	while i > 1:
		for (k, v) in countPrime.items():
			count = 0
			while i % k == 0:
				i /= k
				count += 1
			if count > countPrime[k]:
				countPrime[k] = count

ans = 1
for (k, v) in countPrime.items():
		for i in range(v):
			ans *= k

print ans

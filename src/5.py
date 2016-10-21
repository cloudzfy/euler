# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# 
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

size = 20
is_prime = [True for i in range(size)]

for i in range(2, size):
	if is_prime[i]:
		j = 2
		while i * j < size:
			is_prime[i * j] = False
			j += 1

count_prime = {}
for i in range(2, len(is_prime)):
	if is_prime[i]:
		count_prime[i] = 0

for i in range(2, 21):
	while i > 1:
		for (k, v) in count_prime.items():
			count = 0
			while i % k == 0:
				i /= k
				count += 1
			if count > count_prime[k]:
				count_prime[k] = count

ans = 1
for (k, v) in count_prime.items():
		for i in range(v):
			ans *= k

print ans

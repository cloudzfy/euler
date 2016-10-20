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
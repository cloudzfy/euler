# Starting with 1 and spiralling anticlockwise in the following way,
# a square spiral with side length 7 is formed.

# 37 36 35 34 33 32 31
# 38 17 16 15 14 13 30
# 39 18  5  4  3 12 29
# 40 19  6  1  2 11 28
# 41 20  7  8  9 10 27
# 42 21 22 23 24 25 26
# 43 44 45 46 47 48 49

# It is interesting to note that the odd squares lie along the bottom
# right diagonal, but what is more interesting is that 8 out of the 13
# numbers lying along both diagonals are prime; that is, a ratio of
# 8/13 = 62%.

# If one complete new layer is wrapped around the spiral above, a square
# spiral with side length 9 will be formed. If this process is continued,
# what is the side length of the square spiral for which the ratio of
# primes along both diagonals first falls below 10%?

from random import randrange

def isPrime_miller_rabin(num):
	if num == 2:
		return True
	if num % 2 == 0:
		return False
	d = num - 1
	r = 0
	while d % 2 == 0:
		d /= 2
		r += 1
	for i in range(20):
		a = randrange(2, num, 1)
		x = pow(a, d, num)
		if x == 1 or x == num - 1:
			continue
		isComposite = True
		for j in range(r - 1):
			x = x * x % num
			if x == 1:
				return False
			if x == num - 1:
				isComposite = False
				break
		if isComposite:
			return False
	return True

length = 2
base = 1
count = 0
while True:
	for i in range(1, 4):
		if isPrime_miller_rabin(base + length * i):
			count += 1
	if count * 10 < length * 2 + 1:
		break
	base += length * 4
	length += 2

print length + 1

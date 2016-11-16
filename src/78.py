# Let p(n) represent the number of different ways in whichn coins can
# be separated into piles. For example, five coins can be separated
# into piles in exactly seven different ways, so p(5) = 7.

# OOOOO
# OOOO O
# OOO OO
# OOO O O
# OO OO O
# OO O O O
# O O O O O

# Find the least value of n for which p(n) is divisible by one million.

p = [1]
n = 1

def sgn(x):
	if x % 2 == 0:
		return 1
	else:
		return -1

while p[-1] % 1000000 <> 0:
	p.append(0)
	i = 0
	k = 1
	g = k * (3 * k - 1) / 2
	while g <= n:
		p[n] += sgn(k - 1) * p[n - g]
		i += 1
		k = i / 2 + 1 if i % 2 == 0 else -int(i / 2) - 1
		g = k * (3 * k - 1) / 2
	p[n] %= 1000000
	n += 1

print n

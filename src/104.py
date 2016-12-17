# The Fibonacci sequence is defined by the recurrence relation:

# F_n = F_{n-1} + F_{n-2}, where F_1 = 1 and F_2 = 1.

# It turns out that F541, which contains 113 digits, is the first
# Fibonacci number for which the last nine digits are 1-9 pandigital
# (contain all the digits 1 to 9, but not necessarily in order). And
# F_{2749}, which contains 575 digits, is the first Fibonacci number
# for which the first nine digits are 1-9 pandigital.

# Given that F_k is the first Fibonacci number for which the first
# nine digits AND the last nine digits are 1-9 pandigital, find k.

from math import sqrt
from math import log

f1 = 1
f2 = 1
n = 2

limit = 1000000000

phi = (1 + sqrt(5)) / 2
a = log(phi) / log(10)
b = log(sqrt(5)) / log(10)

while True:
	f1, f2 = f2, (f1 + f2) % limit
	n += 1
	t = n * a - b
	if ''.join(sorted(str(f2)[:9])) == '123456789' and ''.join(sorted(str(int(pow(10, t - int(t) + 8))))) == '123456789':
		break

print n

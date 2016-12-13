# By using each of the digits from the set, {1, 2, 3, 4}, exactly
# once, and making use of the four arithmetic operations (+, -, *, /)
# and brackets/parentheses, it is possible to form different positive
# integer targets.

# For example,

#   8 = (4 * (1 + 3)) / 2
#   14 = 4 * (3 + 1 / 2)
#   19 = 4 * (2 + 3) - 1
#   36 = 3 * 4 * (2 + 1)

# Note that concatenations of the digits, like 12 + 34, are not
# allowed.

# Using the set, {1, 2, 3, 4}, it is possible to obtain thirty-one
# different target numbers of which 36 is the maximum, and each of
# the numbers 1 to 28 can be obtained before encountering the first
# non-expressible number.

# Find the set of four distinct digits, a < b < c < d, for which
# the longest set of consecutive positive integers, 1 to n, can
# be obtained, giving your answer as a string: abcd.

from itertools import combinations
from itertools import permutations
from itertools import product

INF = 2147483647

def compute(a, b, sym):
	if sym == '+':
		return a + b
	if sym == '-':
		return a - b
	if sym == '*':
		return a * b
	if sym == '/':
		if b == 0:
			return INF
		return a / b

ans = ''
n = 0

for nums in combinations([float(x) for x in range(10)], 4):
	ret = set()
	for num in permutations(nums, 4):
		for sym in product('+-*/', repeat=3):
			tmp = []
			tmp.append(compute(compute(compute(num[0], num[1], sym[0]), num[2], sym[1]), num[3], sym[2]))
			tmp.append(compute(compute(num[0], num[1], sym[0]), compute(num[2], num[3], sym[2]), sym[1]))
			tmp.append(compute(compute(num[0], compute(num[1], num[2], sym[1]), sym[0]), num[3], sym[2]))
			tmp.append(compute(num[0], compute(compute(num[1], num[2], sym[1]), num[3], sym[2]), sym[0]))
			tmp.append(compute(num[0], compute(num[1], compute(num[2], num[3], sym[2]), sym[1]), sym[0]))
			for x in tmp:
				if int(x) == x:
					ret.add(x)
	for i in range(1, len(ret) + 1):
		if i not in ret:
			if i - 1 > n:
				ans, n = nums, i - 1
			break

print ''.join([str(int(x)) for x in ans])

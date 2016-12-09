# A natural number, N, that can be written as the sum and
# product of a given set of at least two natural numbers,
# {a1, a2, ... , ak} is called a product-sum number:
# N = a_1 + a_2 + ... + a_k = a_1 x a_2 x ... x a_k.

# For example, 6 = 1 + 2 + 3 = 1 x 2 x 3.

# For a given set of size, k, we shall call the smallest N
# with this property a minimal product-sum number. The
# minimal product-sum numbers for sets of size, k = 2, 3,
# 4, 5, and 6 are as follows.

# k = 2: 4 = 2 x 2 = 2 + 2
# k = 3: 6 = 1 x 2 x 3 = 1 + 2 + 3
# k = 4: 8 = 1 x 1 x 2 x 4 = 1 + 1 + 2 + 4
# k = 5: 8 = 1 x 1 x 2 x 2 x 2 = 1 + 1 + 2 + 2 + 2
# k = 6: 12 = 1 x 1 x 1 x 1 x 2 x 6 = 1 + 1 + 1 + 1 + 2 + 6

# Hence for 2 <= k <= 6, the sum of all the minimal product-sum
# numbers is 4 + 6 + 8 + 12 = 30; note that 8 is only counted
# once in the sum.

# In fact, as the complete set of minimal product-sum numbers
# for 2 <= k <= 12 is {4, 6, 8, 12, 15, 16}, the sum is 61.

# What is the sum of all the minimal product-sum numbers for
# 2 <= k <= 12000?

from math import log
from itertools import combinations_with_replacement

limit = 12000
ans = [2 * k for k in range(12001)]

N = int(log(limit * 2) / log(2))
M = limit * 2

for i in range(1, N + 1):
	print i
	for nums in combinations_with_replacement(range(2, M + 1), i):
		prod = reduce(lambda x, y: x * y, nums)
		if prod > limit:
			continue
		k = prod - sum(nums) + len(nums)
		ans[k] = min(ans[k], prod)
	M = M / 2

print sum(ans[2:])

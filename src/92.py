# A number chain is created by continuously adding the square
# of the digits in a number to form a new number until it has
# been seen before.

# For example,

# 44 -> 32 -> 13 -> 10 -> 1 -> 1
# 85 -> 89 -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 -> 58 -> 89

# Therefore any chain that arrives at 1 or 89 will become stuck
# in an endless loop. What is most amazing is that EVERY starting
# number will eventually arrive at 1 or 89.

# How many starting numbers below ten million will arrive at 89?

from collections import Counter
from math import factorial
from itertools import combinations_with_replacement

def is_ended_eighty_nine(num):
	if num == 0:
		return False
	while num <> 89 and num <> 1:
		num = sum([int(x) ** 2 for x in str(num)])
	return num == 89

ans = 0

for nums in combinations_with_replacement(range(10), 7):
	if is_ended_eighty_nine(sum(x ** 2 for x in nums)):
		count = [v for k, v in Counter(nums).items()]
		ans += factorial(sum(count)) / reduce(lambda x, y: x * y, [factorial(n) for n in count])

print ans

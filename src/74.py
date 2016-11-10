# The number 145 is well known for the property that the sum
# of the factorial of its digits is equal to 145:

# 1! + 4! + 5! = 1 + 24 + 120 = 145

# Perhaps less well known is 169, in that it produces the
# longest chain of numbers that link back to 169; it turns
# out that there are only three such loops that exist:

# 169 -> 363601 -> 1454 -> 169
# 871 -> 45361 -> 871
# 872 -> 45362 -> 872

# It is not difficult to prove that EVERY starting number
# will eventually get stuck in a loop. For example,

# 69 -> 363600 -> 1454 -> 169 -> 363601 (-> 1454)
# 78 -> 45360 -> 871 -> 45361 (-> 871)
# 540 -> 145 (-> 145)

# Starting with 69 produces a chain of five non-repeating
# terms, but the longest non-repeating chain with a starting
# number below one million is sixty terms.

# How many chains, with a starting number below one million,
# contain exactly sixty non-repeating terms?

from math import factorial

fac = [factorial(x) for x in range(0, 10)]

def get_sum_of_factorial(num):
	return sum([fac[int(x)] for x in str(num)])

length = {}
limit = 1000000
for i in range(1, limit):
	if i in length:
		continue
	seq = [i]
	x = i
	count = 1
	while True:
		x = get_sum_of_factorial(x)
		if x in seq:
			break
		if x in length:
			count += length[x]
			break
		count += 1
		seq.append(x)
	for j in seq:
		if j not in length and j < limit:
			length[j] = count
		count -= 1

ans = 0
for k, v in length.items():
	if v == 60:
		ans += 1

print ans

# The following iterative sequence is defined for the set of positive integers:

# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains
# 10 terms. Although it has not been proved yet (Collatz Problem), it is thought
# that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.

chains = {}
def count_chains(num):
	count = 1
	tmp = num
	while tmp <> 1:
		if tmp % 2 == 0:
			tmp /= 2
		else:
			tmp = 3 * tmp + 1
		if chains.get(tmp) <> None:
			count += chains[tmp]
			break
		count += 1
	chains[num] = count
	return count

maxLen = 0
ans = 0

for i in range(1, 1000000):
	thisLen = count_chains(i)
	if maxLen < thisLen:
		maxLen = thisLen
		ans = i

print ans
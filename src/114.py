# A row measuring seven units in length has red blocks with a minimum
# length of three units placed on it, such that any two red blocks
# (which are allowed to be different lengths) are separated by at
# least one black square. There are exactly seventeen ways of doing
# this.

#     B B B B B B B    R R R B B B B    B R R R B B B

#     B B R R R B B    B B B R R R B    B B B B R R R

#     R R R B R R R    R R R R B B B    B R R R R B B

#     B B R R R R B    B B B R R R R    R R R R R B B

#     B R R R R R B    B B R R R R R    R R R R R R B

#     B R R R R R R    R R R R R R R

# How many ways can a row measuring fifty units in length be filled?

# NOTE: Although the example above does not lend itself to the possibility,
# in general it is permitted to mix block sizes. For example, on a row
# measuring eight units in length you could use red (3), black (1), and
# red (4).

n = 50
dp = [0 for i in range(n)]

count = 1
for i in range(n - 2):
	if i >= 4:
		count += dp[i - 2]
	for j in range(2, n - i):
		dp[i + j] += count

print sum(dp) + 1

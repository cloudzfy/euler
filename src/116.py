# A row of five black square tiles is to have a number of its tiles
# replaced with coloured oblong tiles chosen from red (length two),
# green (length three), or blue (length four).

# If red tiles are chosen there are exactly seven ways this can be
# done.

#     R R K K K    K R R K K    K K R R K    K K K R R

#     R R R R K    R R K R R    K R R R R

# If green tiles are chosen there are three ways.

#     G G G K K    K G G G K    K K G G G

# And if blue tiles are chosen there are two ways.

#     K B B B B    B B B B K

# Assuming that colours cannot be mixed there are 7 + 3 + 2 = 12 ways
# of replacing the black tiles in a row measuring five units in length.

# How many different ways can the black tiles in a row measuring fifty
# units in length be replaced if colours cannot be mixed and at least
# one coloured tile must be used?

# NOTE: This is related to Problem 117.

n = 50
ans = 0
for c in range(2, 5):
	dp = [0 for i in range(n)]
	count = 1
	for i in range(n - c + 1):
		dp[i + c - 1] += count
		count += dp[i]
	ans += sum(dp)

print ans

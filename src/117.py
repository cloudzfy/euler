# Using a combination of black square tiles and oblong tiles chosen
# from: red tiles measuring two units, green tiles measuring three
# units, and blue tiles measuring four units, it is possible to tile
# a row measuring five units in length in exactly fifteen different
# ways.

#     K K K K K    R R K K K    K R R K K    K K R R K

#     K K K R R    R R R R K    R R K R R    K R R R R

#     G G G K K    K G G G K    K K G G G    R R G G G

#     G G G R R    B B B B K    K B B B B

# How many ways can a row measuring fifty units in length be tiled?

# NOTE: This is related to Problem 116.

n = 50
dp = [0 for i in range(n)]
count = 1
for i in range(n):
	for c in range(2, 5):
		if i + c - 1 < n:
			dp[i + c - 1] += count
	count += dp[i]

print sum(dp) + 1

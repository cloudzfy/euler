# The cube, 41063625 (345^3), can be permuted to produce two other
# cubes: 56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is
# the smallest cube which has exactly three permutations of its
# digits which are also cube.

# Find the smallest cube for which exactly five permutations of its
# digits are cube.

ans = 346
cubes = {}
counts = {}

while True:
	cube = pow(ans, 3)
	tmp = ''.join(sorted(str(cube)))
	if tmp in counts:
		counts[tmp] += 1
		if counts[tmp] == 5:
			print pow(cubes[tmp], 3)
			break
	else:
		counts[tmp] = 1
		cubes[tmp] = ans
	ans += 1

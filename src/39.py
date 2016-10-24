# If p is the perimeter of a right angle triangle with integral length
# sides, {a,b,c}, there are exactly three solutions for p = 120.

# {20,48,52}, {24,45,51}, {30,40,50}

# For which value of p <= 1000, is the number of solutions maximised?

def get_right_triangle_solutions(perimeter):
	count = 0
	for a in range(1, perimeter / 2):
		if (p * p - 2 * p * a) % (2 * p - 2 * a) == 0:
			count += 1
	return count

ans = 0
solutions = 0
for p in range(4, 1001):
	s = get_right_triangle_solutions(p)
	if s > solutions:
		ans, solutions = p, s

print ans

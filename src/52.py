# It can be seen that the number, 125874, and its double, 251748,
# contain exactly the same digits, but in a different order.

# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x,
# and 6x, contain the same digits.

def is_permuted_multiple(num):
	for i in range(2, 7):
		if sorted(str(num * i)) <> sorted(str(num)):
			return False
	return True

i = 1
while True:
	if is_permuted_multiple(i):
		print i
		break
	i += 1

# A permutation is an ordered arrangement of objects. For example, 3124
# is one possible permutation of the digits 1, 2, 3 and 4. If all of the
# permutations are listed numerically or alphabetically, we call it
# lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

# 012   021   102   120   201   210

# What is the millionth lexicographic permutation of the digits 0, 1, 2,
# 3, 4, 5, 6, 7, 8 and 9?

def next_permutation(num):
	length = len(num)
	pos = -1
	for i in range(length - 2, -1, -1):
		if num[i] < num[i + 1]:
			pos = i
			break
	if pos == -1:
		num.sort()
		return num
	mark = num[pos]
	for i in range(length - 1, pos, -1):
		if num[i] > mark:
			num[pos], num[i] = num[i], num[pos]
			break
	num[pos + 1:] = sorted(num[pos + 1:])
	return num

digits = list('0123456789')
for i in range(1000000 - 1):
	digits = next_permutation(digits)

print ''.join(digits)

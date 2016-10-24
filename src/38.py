# Take the number 192 and multiply it by each of 1, 2, and 3:

# 192 x 1 = 192
# 192 x 2 = 384
# 192 x 3 = 576
# By concatenating each product we get the 1 to 9 pandigital, 192384576.
# We will call 192384576 the concatenated product of 192 and (1,2,3)

# The same can be achieved by starting with 9 and multiplying by 1, 2, 3,
# 4, and 5, giving the pandigital, 918273645, which is the concatenated
# product of 9 and (1,2,3,4,5).

# What is the largest 1 to 9 pandigital 9-digit number that can be formed
# as the concatenated product of an integer with (1,2, ... , n) where
# n > 1?

def get_pandigital_multiple(num):
	ret = str(num)
	n = 2
	while len(ret) < 9:
		ret += str(num * n)
		n += 1
	return ret[:9]

ans = 0
for i in range(1, 10000):
	ret = get_pandigital_multiple(i)
	if ''.join(sorted(ret)) == '123456789' and ret > ans:
		ans = ret

print ans

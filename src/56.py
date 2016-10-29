# A googol (10^100) is a massive number: one followed by one-hundred zeros;
# 100^100 is almost unimaginably large: one followed by two-hundred zeros.
# Despite their size, the sum of the digits in each number is only 1.

# Considering natural numbers of the form, ab, where a, b < 100, what is the
# maximum digital sum?

def get_digital_sum(num):
	return sum([int(x) for x in str(num)])

ans = 0
for a in range(1, 100):
	for b in range(1, 100):
		ans = max(ans, get_digital_sum(pow(a, b)))

print ans

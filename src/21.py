# Let d(n) be defined as the sum of proper divisors of n (numbers
# less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a != b, then a and b are an amicable
# pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20,
# 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of
# 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.

def d(num):
	ret = 0
	for i in range(1, num / 2 + 1):
		if num % i == 0:
			ret += i
	return ret

amicable = {}

for i in range(1, 10000):
	if amicable.get(i) != None:
		continue
	j = d(i)
	if i == j or d(j) <> i:
		amicable[i] = False
	else:
		amicable[i] = True
		amicable[j] = True

print sum(filter(lambda x: amicable[x], range(1, 10000)))
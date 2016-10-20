sum1 = 0
for i in range(1, 101):
	sum1 += i * i

sum2 = 0
for i in range(1, 101):
	sum2 += i

sum2 *= sum2

print sum2 - sum1
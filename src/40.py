# An irrational decimal fraction is created by concatenating the
# positive integers:

# 0.123456789101112131415161718192021...

# It can be seen that the 12th digit of the fractional part is 1.

# If dn represents the nth digit of the fractional part, find the
# value of the following expression.

# d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000

fraction = ''

count = 0
while len(fraction) < 1000001:
	fraction += str(count)
	count += 1

j = 1
ans = 1
for i in range(7):
	ans *= int(fraction[j])
	j *= 10

print ans

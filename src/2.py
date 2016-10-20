a = 1
b = 2
ans = 2

while b <= 4000000:
	a = a + b
	tmp = a
	a = b
	b = tmp
	if b % 2 == 0:
		ans += b

print ans
# The 5-digit number, 16807 = 7^5, is also a fifth power.
# Similarly, the 9-digit number, 134217728 = 8^9, is a
# ninth power.

# How many n-digit positive integers exist which are
# also an nth power?

count = 0
for base in range(1, 10):
	idx = 1
	while True:
		length = len(str(pow(base, idx)))
		if length == idx:
			count += 1
		elif length < idx:
			break
		idx += 1

print count

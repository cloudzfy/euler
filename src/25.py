# The Fibonacci sequence is defined by the recurrence relation:

# F_n = F_{n-1} + F_{n-2}, where F_1 = 1 and F_2 = 1.
# Hence the first 12 terms will be:

# F_1 = 1
# F_2 = 1
# F_3 = 2
# F_4 = 3
# F_5 = 5
# F_6 = 8
# F_7 = 13
# F_8 = 21
# F_9 = 34
# F_10 = 55
# F_11 = 89
# F_12 = 144
# The 12th term, F_12, is the first term to contain three digits.

# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

count = 2
a = 1
b = 1
while len(str(b)) < 1000:
	a = a + b
	a, b = b, a
	count += 1

print count
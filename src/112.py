# Working from left-to-right if no digit is exceeded by the digit
# to its left it is called an increasing number; for example,
# 134468.

# Similarly if no digit is exceeded by the digit to its right it
# is called a decreasing number; for example, 66420.

# We shall call a positive integer that is neither increasing nor
# decreasing a "bouncy" number; for example, 155349.

# Clearly there cannot be any bouncy numbers below one-hundred,
# but just over half of the numbers below one-thousand (525) are
# bouncy. In fact, the least number for which the proportion of
# bouncy numbers first reaches 50% is 538.

# Surprisingly, bouncy numbers become more and more common and by
# the time we reach 21780 the proportion of bouncy numbers is
# equal to 90%.

# Find the least number for which the proportion of bouncy numbers
# is exactly 99%.

def is_bouncy_number(num):
	asc = 0
	dec = 0
	for i in range(1, len(num)):
		if num[i - 1] <= num[i]:
			asc += 1
		if num[i - 1] >= num[i]:
			dec += 1
	return asc <> len(num) - 1 and dec <> len(num) - 1

total = 1
bouncy = 0

while bouncy * 100 < 99 * total:
	total += 1
	if is_bouncy_number(str(total)):
		bouncy += 1

print total

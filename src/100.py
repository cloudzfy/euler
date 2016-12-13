# If a box contains twenty-one coloured discs, composed
# of fifteen blue discs and six red discs, and two discs
# were taken at random, it can be seen that the probability
# of taking two blue discs, P(BB) = (15/21)x(14/20) = 1/2.

# The next such arrangement, for which there is exactly
# 50% chance of taking two blue discs at random, is a box
# containing eighty-five blue discs and thirty-five red
# discs.

# By finding the first arrangement to contain over
# 10^12 = 1,000,000,000,000 discs in total, determine
# the number of blue discs that the box would contain.

x = 1
y = 1
limit = 1000000000000

while True:
	if x % 2 == 1 and y % 2 == 1:
		if (x + 1) / 2 > limit:
			print (y + 1) / 2
			break
	x, y = 3 * x + 4 * y, 2 * x + 3 * y
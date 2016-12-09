# For a number written in Roman numerals to be considered valid
# there are basic rules which must be followed. Even though the
# rules allow some numbers to be expressed in more than one way
# there is always a "best" way of writing a particular number.

# For example, it would appear that there are at least six ways
# of writing the number sixteen:

#   IIIIIIIIIIIIIIII
#   VIIIIIIIIIII
#   VVIIIIII
#   XIIIIII
#   VVVI
#   XVI

# However, according to the rules only XIIIIII and XVI are valid,
# and the last example is considered to be the most efficient, as
# it uses the least number of numerals.

# The 11K text file, roman.txt (right click and 'Save Link/Target
# As...'), contains one thousand numbers written in valid, but not
# necessarily minimal, Roman numerals; see About... Roman Numerals
# for the definitive rules for this problem.

# Find the number of characters saved by writing each of these in
# their minimal form.

# Note: You can assume that all the Roman numerals in the file
# contain no more than four consecutive identical units.

romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

ones      = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
tens      = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
hundreds  = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
thousands = ['', 'M', 'MM', 'MMM', 'MMMM']

def roman_to_num(text):
	ret = romans[text[-1]]
	for i in range(1, len(text)):
		if romans[text[i - 1]] < romans[text[i]]:
			ret -= romans[text[i - 1]]
		else:
			ret += romans[text[i - 1]]
	return ret

def num_to_roman(num):
	ret = thousands[num / 1000]
	num %= 1000
	ret += hundreds[num / 100]
	num %= 100
	ret += tens[num / 10]
	num %= 10
	ret += ones[num]
	return ret

file = open('../data/p089_roman.txt', 'r')
data = file.read()
file.close()

ans = 0
for x in data.split('\n'):
	ans += len(x)
	ans -= len(num_to_roman(roman_to_num(x)))

print ans

# The nth term of the sequence of triangle numbers is given by,
# t_n = 1/2 * n (n + 1); so the first ten triangle numbers are:

# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# By converting each letter in a word to a number corresponding
# to its alphabetical position and adding these values we form
# a word value. For example, the word value for SKY is 19 + 11
# + 25 = 55 = t10. If the word value is a triangle number then
# we shall call the word a triangle word.

# Using words.txt (right click and 'Save Link/Target As...'),
# a 16K text file containing nearly two-thousand common English
# words, how many are triangle words?

from math import sqrt

file = open('../data/p042_words.txt', 'r')
data = file.read()
file.close()

words = data.replace('"', '').split(',')

def is_triangle_number(num):
	n = int(sqrt(num * 2))
	return n * (n + 1) == num * 2

ans = []
for w in words:
	num = sum([ord(x) - ord('A') + 1 for x in list(w)])
	if is_triangle_number(num):
		ans.append(num)

print len(ans)

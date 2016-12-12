# By replacing each of the letters in the word CARE with 1, 2,
# 9, and 6 respectively, we form a square number: 1296 = 362.
# What is remarkable is that, by using the same digital
# substitutions, the anagram, RACE, also forms a square number:
# 9216 = 962. We shall call CARE (and RACE) a square anagram
# word pair and specify further that leading zeroes are not
# permitted, neither may a different letter have the same
# digital value as another letter.

# Using words.txt (right click and 'Save Link/Target As...'),
# a 16K text file containing nearly two-thousand common English
# words, find all the square anagram word pairs (a palindromic
# word is NOT considered to be an anagram of itself).

# What is the largest square number formed by any member of
# such a pair?

# NOTE: All anagrams formed must be contained in the given
# text file.

from string import maketrans

file = open('../data/p098_words.txt', 'r')
data = file.read()
file.close()

strings = data.replace('"', '').split(',')

anagrams = {}
for s in strings:
	tmp = ''.join(sorted(s))
	if tmp not in anagrams:
		anagrams[tmp] = [s]
	else:
		anagrams[tmp].append(s)

pairs = [s[1] for s in filter(lambda x: len(x[1]) > 1, anagrams.items())]

ans = 0
for pair in pairs:
	nums = set(filter(lambda x: len((str(x))) == len(pair[0]), [x**2 for x in range(40000)]))
	for num in nums:
		tmp1 = pair[1].translate(maketrans(pair[0], str(num)))
		tmp2 = tmp1.translate(maketrans(str(num), pair[0]))
		if tmp2 == pair[1] and int(tmp1) in nums:
			ans = max(ans, max(int(tmp1), num))

print ans

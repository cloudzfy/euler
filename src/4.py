# A palindromic number reads the same both ways. The largest palindrome made from 
# the product of two 2-digit numbers is 9009 = 91 × 99.
# 
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(num):
	text = str(num)
	i = 0
	j = len(text) - 1
	while i < j:
		if text[i] <> text[j]:
			return False
		i += 1
		j -= 1
	return True

ans = 0
for i in range(100, 1000):
	for j in range(100, 1000):
		if is_palindrome(i * j) and ans < i * j:
			ans = i * j

print ans

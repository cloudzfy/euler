# The decimal number, 585 = 1001001001_2 (binary), is palindromic
# in both bases.

# Find the sum of all numbers, less than one million, which are
# palindromic in base 10 and base 2.

# (Please note that the palindromic number, in either base, may
# not include leading zeros.)

def is_palindrome(num):
	return num[::-1] == num

ans = []
for i in range(1000000):
	if is_palindrome(str(i)) and is_palindrome(bin(i)[2:]):
		ans.append(i)

print sum(ans)

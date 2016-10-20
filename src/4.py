def isPalindrome(num):
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
		if isPalindrome(i * j) and ans < i * j:
			ans = i * j

print ans

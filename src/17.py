# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out
# in words, how many letters would be used?

# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
# forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
# 20 letters. The use of "and" when writing out numbers is in compliance with
# British usage.

nums1 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
nums2 = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
nums3 = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
nums4 = ['hundred', 'thousand', 'and']

def sayNumber(num):
	text = ''
	if num >= 1000:
		text += nums1[num / 1000 - 1] + nums4[1]
		num %= 1000
		if num > 0 and num < 100:
			text += nums4[2]
	if num >= 100:
		text += nums1[num / 100 - 1] + nums4[0]
		num %= 100
		if num > 0:
			text += nums4[2]
	if num >= 20:
		text += nums3[num / 10 - 2]
		num %= 10
		if num > 0:
			text += nums1[num - 1]
	elif num > 10:
		text += nums2[num - 11]
	elif num > 0:
		text += nums1[num - 1]
	return len(text)

ans = 0
for i in range(1, 1001):
	ans += sayNumber(i)

print ans
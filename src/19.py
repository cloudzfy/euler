# You are given the following information, but you may prefer to
# do some research for yourself.

# * 1 Jan 1900 was a Monday.
# * Thirty days has September,
#   April, June and November.
#   All the rest have thirty-one,
#   Saving February alone,
#   Which has twenty-eight, rain or shine.
#   And on leap years, twenty-nine.
# * A leap year occurs on any year evenly divisible by 4, but not
#   on a century unless it is divisible by 400.

# How many Sundays fell on the first of the month during the twentieth
# century (1 Jan 1901 to 31 Dec 2000)?

months1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
months2 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isLeap(year):
	if year % 100 == 0:
		return year % 400 == 0
	else:
		return year % 4 == 0

day = 1
if isLeap(1900):
	day = (day + sum(months2)) % 7
else:
	day = (day + sum(months1)) % 7

count = 0
for year in range(1901, 2001):
	for month in months2 if isLeap(year) else months1:
		if day == 0:
			count += 1
		day = (day + month) % 7

print count

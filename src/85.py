# By counting carefully it can be seen that a rectangular
# grid measuring 3 by 2 contains eighteen rectangles:

#   #--    ##-    ###
#   ---    ---    ---
#    6      4      2

#   #--    ##-    ###
#   #--    ##-    ###
#    3      2      1

#  [../img/p085.gif]

# Although there exists no rectangular grid that contains
# exactly two million rectangles, find the area of the grid
# with the nearest solution.

n = 2000
m = 1
limit = 2000000
count = 0
diff = abs(limit - count)
ans = 0

while n >= m:
	tmp = n * (n + 1) * m * (m + 1) / 4
	if abs(tmp - limit) < diff:
		diff = abs(tmp - limit)
		count = tmp
		ans = m * n
	if tmp > limit:
		n -= 1
	else:
		m += 1

print ans

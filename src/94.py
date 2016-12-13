# It is easily proved that no equilateral triangle exists with
# integral length sides and integral area. However, the almost
# equilateral triangle 5-5-6 has an area of 12 square units.

# We shall define an almost equilateral triangle to be a triangle
# for which two sides are equal and the third differs by no more
# than one unit.

# Find the sum of the perimeters of all almost equilateral triangles
# with integral side lengths and area and whose perimeters do not
# exceed one billion (1,000,000,000).

limit = 1000000000

x = 2
y = 1
ans = 0

while True:
	if 2 * x - 2 <= limit:
		a = float(2 * x - 1) / 3
		b = a - 1
		if int(a) == a and a > 0 and b > 0:
			ans += 2 * x - 2
	if 2 * x + 2 <= limit:
		a = float(2 * x + 1) / 3
		b = a + 1
		if int(a) == a and a > 1 and b > 0:
			ans += 2 * x + 2
	else:
		break
	x, y = 2 * x + y * 3, 2 * y + x

print ans

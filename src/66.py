# Consider quadratic Diophantine equations of the form:

# x^2 - Dy^2 = 1

# For example, when D = 13, the minimal solution in x is
# 649^2 - 13 x 180^2 = 1.

# It can be assumed that there are no solutions in positive
# integers when D is square.

# By finding minimal solutions in x for D = {2, 3, 5, 6, 7},
# we obtain the following:

# 3^2 - 2 x 2^2 = 1
# 2^2 - 3 x 1^2 = 1
# 9^2 - 5 x 4^2 = 1
# 5^2 - 6 x 2^2 = 1
# 8^2 - 7 x 3^2 = 1

# Hence, by considering minimal solutions in x for D <= 7, the
# largest x is obtained when D = 5.

# Find the value of D <= 1000 in minimal solutions of x for
# which the largest value of x is obtained.

from math import sqrt

def get_fundamental_solution(D):
	a0 = int(sqrt(D))
	m = 0
	d = 1
	a = a0
	p1 = 1
	q1 = 0
	p = a
	q = 1
	while p * p - D * q * q <> 1:
		m = d * a - m
		d = (D - m * m) / d
		a = int((a0 + m) / d)
		p, p1 = a * p + p1, p
		q, q1 = a * q + q1, q
	return p

def is_square(D):
	return int(sqrt(D)) == sqrt(D)

ans = 0
sol = 0

for D in range(2, 1001):
	if not is_square(D):
		ret = get_fundamental_solution(D)
		if ret > sol:
			ans, sol = D, ret

print ans

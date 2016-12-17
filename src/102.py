# Three distinct points are plotted at random on a Cartesian plane,
# for which -1000 <= x, y <= 1000, such that a triangle is formed.

# Consider the following two triangles:

# A(-340,495), B(-153,-910), C(835,-947)

# X(-175,41), Y(-421,-714), Z(574,-645)

# It can be verified that triangle ABC contains the origin, whereas
# triangle XYZ does not.

# Using triangles.txt (right click and 'Save Link/Target As...'),
# a 27K text file containing the co-ordinates of one thousand "random"
# triangles, find the number of triangles for which the interior
# contains the origin.

# NOTE: The first two examples in the file represent the triangles
# in the example given above.

file = open('../data/p102_triangles.txt', 'r')
data = file.read()
file.close()

coords = [[int(x) for x in line.split(',')] for line in data.split('\n')[:-1]]

def cross(A, B):
	return A[0] * B[1] - A[1] * B[0]

def minus(A, B):
	return [A[0] - B[0], A[1] - B[1]]

def contain_origin(coord):
	A = coord[0:2]
	B = coord[2:4]
	C = coord[4:6]
	O = [0, 0]
	for i in range(0, 6, 2):
		if cross(minus(coord[i:i+2], coord[(i+2)%6:(i+3)%6+1]), \
			minus(O, coord[(i+2)%6:(i+3)%6+1])) \
			* cross(minus(coord[(i+4)%6:(i+5)%6+1], coord[(i+2)%6:(i+3)%6+1]), \
			minus(O, coord[(i+2)%6:(i+3)%6+1])) >=0:
			return False
	return True

print sum([1 if contain_origin(coord) else 0 for coord in coords])

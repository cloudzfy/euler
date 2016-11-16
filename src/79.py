# A common security method used for online banking is to ask
# the user for three random characters from a passcode. For
# example, if the passcode was 531278, they may ask for the
# 2nd, 3rd, and 5th characters; the expected reply would be:
# 317.

# The text file, keylog.txt, contains fifty successful login
# attempts.

# Given that the three characters are always asked for in
# order, analyse the file so as to determine the shortest
# possible secret passcode of unknown length.

file = open('../data/p079_keylog.txt')
data = file.read()
file.close()

keys = data.split('\n')[:-1]
ans = []

while len(keys) > 0:
	head = set()
	rest = set()
	for k in keys:
		head.add(k[0])
		if len(k) > 1:
			rest.add(k[1])
			if len(k) > 2:
				rest.add(k[2])
	for i in head:
		if i not in rest:
			newkeys = []
			for k in keys:
				newkeys.append(k.replace(i, ''))
			keys = [k for k in newkeys if len(k) > 0]
			ans += i
			break

print ''.join(ans)

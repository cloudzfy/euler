# The radical of n, rad(n), is the product of distinct prime factors of
# n. For example, 504 = 2^3 x 3^2 x 7, so rad(504) = 2 x 3 x 7 = 42.

# We shall define the triplet of positive integers (a, b, c) to be an
# abc-hit if:

#   1. GCD(a, b) = GCD(a, c) = GCD(b, c) = 1
#   2. a < b
#   3. a + b = c
#   4. rad(abc) < c

# For example, (5, 27, 32) is an abc-hit, because:

#   1. GCD(5, 27) = GCD(5, 32) = GCD(27, 32) = 1
#   2. 5 < 27
#   3. 5 + 27 = 32
#   4. rad(4320) = 30 < 32

# It turns out that abc-hits are quite rare and there are only
# thirty-one abc-hits for c < 1000, with sum(c) = 12523.

# Find sum(c) for c < 120000.


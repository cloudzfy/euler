# Consider the infinite polynomial series A_G(x) = x * G_1
# + x^2 * G_2 + x^3 * G_3 + ..., where G_k is the kth term
# of the second order recurrence relation G_k = G_{k−1} +
# G_{k−2}, G_1 = 1 and G_2 = 4; that is, 1, 4, 5, 9, 14,
# 23, ... .

# For this problem we shall be concerned with values of x
# for which A_G(x) is a positive integer.

# The corresponding values of x for the first five natural
# numbers are shown below.

#     x                         A_G(x)
#     (sqrt(5) - 1) / 4         1
#     2 / 5                     2
#     (sqrt(22) - 2) / 6        3
#     (sqrt(137) - 5) / 14      4
#     1 / 2                     5

# We shall call A_G(x) a golden nugget if x is rational,
# because they become increasingly rarer; for example,
# the 20th golden nugget is 211345365.

# Find the sum of the first thirty golden nuggets.
# In the card game poker, a hand consists of five cards and are ranked,
# from lowest to highest, in the following way:

# * High Card: Highest value card.
# * One Pair: Two cards of the same value.
# * Two Pairs: Two different pairs.
# * Three of a Kind: Three cards of the same value.
# * Straight: All cards are consecutive values.
# * Flush: All cards of the same suit.
# * Full House: Three of a kind and a pair.
# * Four of a Kind: Four cards of the same value.
# * Straight Flush: All cards are consecutive values of same suit.
# * Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

# The cards are valued in the order:
# 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

# If two players have the same ranked hands then the rank made up of the
# highest value wins; for example, a pair of eights beats a pair of fives
# (see example 1 below). But if two ranks tie, for example, both players
# have a pair of queens, then highest cards in each hand are compared
# (see example 4 below); if the highest cards tie then the next highest
# cards are compared, and so on.

# Consider the following five hands dealt to two players:

# Hand        Player 1	 	      Player 2              Winner
# 1           5H 5C 6S 7S KD        2C 3S 8S 8D TD        Player 2
#             Pair of Fives         Pair of Eights
# 2           5D 8C 9S JS AC        2C 5C 7D 8S QH        Player 1
#             Highest card Ace      Highest card Queen
# 3           2D 9C AS AH AC        3D 6D 7D TD QD        Player 2
#             Three Aces            Flush with Diamonds
# 4           4D 6S 9H QH QC        3D 6D 7H QD QS        Player 1
#             Pair of Queens        Pair of Queens
#             Highest card Nine     Highest card Seven
# 5           2H 2D 4C 4D 4S        3C 3D 3S 9S 9D        Player 1
#             Full House            Full House
#             With Three Fours      with Three Threes

# The file, poker.txt, contains one-thousand random hands dealt to two
# players. Each line of the file contains ten cards (separated by a
# single space): the first five are Player 1's cards and the last five
# are Player 2's cards. You can assume that all hands are valid (no
# invalid characters or repeated cards), each player's hand is in no
# specific order, and in each hand there is a clear winner.

# How many hands does Player 1 win?

from collections import Counter

consecutive = [(v, v - 1, v - 2, v - 3, v - 4) for v in range(6, 15)]
kind = [(1, 1, 1, 1, 1), (2, 1, 1, 1), (2, 2, 1), (3, 1, 1), (), (), (3, 2), (4, 1)]
value = {'23456789TJQKA'[i - 2]: i for i in range(2, 15)}

def get_card_values(cards):
	nums = zip(*sorted([(v, k) for k, v in Counter(value[x[0]] for x in cards).items()], reverse=True))
	ret = [kind.index(nums[0]), nums[1]]
	if len(set(x[1] for x in cards)) == 1:
		ret[0] = 5
	if nums[1] in consecutive:
		if ret[0] == 5:
			ret[0] = 8
			if min(nums[1]) == 10:
				ret[0] = 9
		else:
			ret[0] = 4
	return ret

file = open('../res/p054_poker.txt')
ans = 0
for line in file.readlines():
	cards = line.split(' ')
	if get_card_values(cards[0:5]) > get_card_values(cards[5:10]):
		ans += 1

print ans

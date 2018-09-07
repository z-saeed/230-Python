#cardGame.py
#basic card game framework
#keeps track of card locations for as many hands as needed

import random

NUMCARDS = 52
DECK = 0
PLAYER = 1
COMP = 2

cardLoc = [0] * NUMCARDS
suitName = ("hearts", "diamonds", "spades", "clubs")
rankName = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven", 
			"Eight", "Nine", "Ten", "Jack", "Queen", "King")
playerName = ("deck", "player", "computer")

cardList = []

def clearDeck():

	global cardLoc
	cardLoc = [0] * NUMCARDS

	x = 0
	for i in suitName:
		for j in rankName:
			x += 1

			cardList.append((x, j, i))

def assignCard(hand):
	
	randSuit = random.randint(0, len(suitName) - 1)
	randRank = random.randint(0, len(rankName) - 1)

	rank = rankName[randRank]
	suit = suitName[randSuit]

	for x, y, z in cardList:
		if rank == y and suit == z:
			cardLoc[x - 1] = hand

def showDeck():

	print("\n#  Card \t\tLocation")
	
	for x, y, z in cardList:
		if cardLoc[x - 1] == 0:
			print("{} {} of {} \tDECK".format(x, y, z))
		elif cardLoc[x - 1] == 1:
			print("{} {} of {} \tPLAYER".format(x, y, z))
		elif cardLoc[x - 1] == 2:
			print("{} {} of {} \tCOMPUTER".format(x, y, z))
		else:
			print("Weird, I can't find that card...")

def showHand(hand):

	if hand == 1:
		print("\nPlayer Hand:")
	elif hand == 2:
		print("\nComputer Hand:")
	else:
		print("Something went wrong")

	x = 0
	for i in cardLoc:
		if hand == i:
			card = cardList[x]
			print(card[1] + " of " + card[2])
		x += 1

def menu():

	exit = input("\nPress 1 to continue: ")

	return exit

def main():

	keepGoing = True
	while keepGoing:
		clearDeck()

		for i in range(5):
			assignCard(PLAYER)
			assignCard(COMP)

		showDeck()
		showHand(PLAYER)
		showHand(COMP)

		exit = menu()

		if exit != '1':
			keepGoing = False

if __name__ == __main__:
	main()
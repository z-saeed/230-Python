#highLow.py
#Zaid Saeed
#Randomly generate a number and have the user try and guess what the number is
#Tell user if their guess is too high or too low and how many turns it took to guess the correct number

import random

#Function for User guesses
def userGuess(count):

	correct = True
	while (correct):

		#Recieve User's Guess
		guess = 0

		#Make sure User inputs number
		tryCatch = True 
		while tryCatch:

			try:

				#Recieve User's Guess
				guess = input("{}) Please enter a number\n".format(count))

				#Convert guess to int for comparisions
				guess = int(guess)

				tryCatch = False

			except ValueError:

				#If value is not a number, tell User
				print("That is not a number\n")
			
		#Calculate if User's guess is greater than or lower than randomly generated number
		if guess > rand:
			print("Too High!\n")
		elif guess < rand:
			print ("Too Low!\n")
		else:
			correct = False

		#Increase count by one each time
		count += 1

	#Return number of tries
	return count

keepGoing = True
while (keepGoing): #loop

	#Initiate count at 1
	count = 1

	#Generate Random Number from 1 to 100
	rand = random.randint(1, 100) #Test

	print("I'm thinking of a number between 1 and 100.\nGuess a number and I will tell you if you're too high,\ntoo low, or got it right!\nGood Luck!\n")

	#Initiate Funtion; Takes number of Tries returned from Function and puts it in count
	count = userGuess(count)

	#Output number of tries
	print("\n\nCorrect!\nTook you {} turns\n".format(count - 1))

	#Ask User if they want to continue
	exit = input("Press 1 to exit or press anything else to continue:\n")

	#Check User's response
	if exit == '1':
		keepGoing = False





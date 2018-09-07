#blackBelt.py
#Zaid Saeed
#Guess what number the user is thinking
#Takes User's input to decide whether guess was too high, too low, or correct

import random

#Set x value at 100, y value at 1, and count at 1
x = 100
y = 1
count = 1

#Recieve random number using x and y values
rand = random.randint(y,x)

print("\nPlease think of a number between one and one hundred. \nI'll guess your number. You tell me if I'm too high, \ntoo low, or correct.")

keepGoing = True
while keepGoing:
	
	#Get User's respose if guess was too high, low, or if guess was correct
	response = input("I guess: {}\nAm I too (h)igh, too (l)ow, or (c)orrect?".format(rand))

	#If User's response is too high
	if response == 'h':

		#x equaled guessed number - 1
		x = rand - 1

		#Get new random guessed number with the new x value
		rand = random.randint(y, x)

		#Increase count by 1
		count += 1

	#If User's response is too low
	elif response == 'l':

		#y equaled to guess number + 1
		y = rand + 1

		#Get new random guessed number with new y value
		rand = random.randint(y, x)

		#Increase count by 1
		count += 1

	#If User's response is correct
	elif response == 'c':

		#Output number of tries it took
		print("Yay, it took me {} tries".format(count))

		#Exit Loop
		keepGoing = False

	#If User's response is none of the above
	else:
		print("sorry I dont understand")









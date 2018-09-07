import random

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_-+=[]{};:,.<>/?`~"
key = "X~P`M!G#T@D$HL%^Y&O*N(Z)B_W-E+A={}[]RK:;JU,.FS<>/?CIQV"

keyList = []

#Menu function
def menu():

	print("\n0) Quit\n1) Encode\n2) Decode\n")

	response = input("What do you want to do? ")
	return(response)

#Encrypting function
def encode(text):

	#Scramble Key
	global key
	key = ''.join(random.sample(key, len(key)))

	#Return a translation table from Alpha to scrambled key
	switch = alpha.maketrans(alpha + alpha.lower(), key*2)

	#Encrypt text
	encodeText = text.translate(switch)

	#Add scrambled key and encrypted text to keyList
	keyList.append((key, encodeText))

	#Return encrypted text
	return(encodeText)

#Decrypting function
def decode(text):

	#initialze variable
	switch = ''

	#Iterate through keyList
	for x, y in keyList:

		#Compare User's inputted encrypted string to encrypted strings in keyList
		if (text.upper() == y.upper()):

			#Return a translation table from keyList key to Alpha key
			switch = alpha.maketrans(x + x.lower(), alpha + alpha.lower())
	
	#Decode string
	decodeText = text.translate(switch)

	#Return decoded String
	decodeText = decodeText.upper()
	return(decodeText)

#Main function
def main():

	keepGoing = True
	while keepGoing:

		response = menu()
		if response == '1':

			plain = input("text to be encoded: ")
			print (encode(plain))

		elif response == '2':

			coded = input("code to be decyphered: ")
			print (decode(coded))

		elif response == '0':

			print ("\nthanks for doing secret spy stuff with me.")
			keepGoing = False

		else:

			print ("\nI dont know what you want to do...\n")


if __name__=="__main__":
	main()

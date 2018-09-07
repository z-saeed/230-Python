import random

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ `~!@#$%^&*()_-+=[]{};:,./<>?1234567890"
key = "XPMGTDHLYONZ`~!@#$%^&*()_-+=[]{};:,./<>?BWEARKJUFS CIQV1234567890"

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

	encryptText = ''

	#iterate through text string
	for i in text:
		#Find key value when alpha letter equals i and add to encryptText string
		encryptText += key[alpha.find(i.upper())]

	#Add encryptText and key used to encrypt into list
	keyList.append((key, encryptText))
	return(encryptText)

#Decrypting function
def decode(text):

	decryptText = ''

	#iterate through key list
	for keys, enText in keyList:
		#find when user submitted stirng equals on of the strings in keylist
		if enText.upper() == text.upper():
			#have key equal the key from keylist
			key = keys
			#iterate through text string
			for i in text:
				#Find key value when key letter equals i and add to decryptText string
				decryptText += alpha[key.find(i.upper())]
			#remove key and encrypt text from list
			keyList.remove((key, enText))

	if text not in keyList:
		print("please enter a valid number")

	return(decryptText)

#Main function
def main():

	keepGoing = True
	while keepGoing:

		response = menu()
		if response == '1':

			plain = input("Text to be encoded: ")
			print ("\n", encode(plain))

		elif response == '2':

			print("\nCODE NOT CASE SENSITIVE")
			coded = input("Code to be decyphered: ")
			print ("\n", decode(coded))

		elif response == '0':

			print ("\nThanks for doing secret spy stuff with me.")
			keepGoing = False

		elif response.upper() == 'KEYLIST':

			print(keyList)

		else:

			print ("\nI dont know what you want to do...\n")


if __name__=="__main__":
	main()

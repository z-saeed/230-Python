price = input("Price of item: \n")
cash = input("\nCash tendered: \n")

price = float(price)
cash = float(cash)
change = 0
twenty = 0
ten = 0
five = 0
one = 0
quarter = 0
dime = 0
nickle = 0
penny = 0

price *= 100
cash *= 100

price = int(price)
cash = int(cash)
 
if cash > price:
	change = cash - price
else:
	print("Please pay the total amount")
	exit()

change = float(change)

changeOut = change / 100

keepGoing = True
while keepGoing:
	if change >= 2000:
		change -= 2000
		twenty += 1
	elif change >= 1000:
		change -= 1000
		ten += 1
	elif change >= 500:
		change -= 500
		five += 1
	elif change >= 100:
		change -= 100
		one += 1
	elif change >= 25:
		change -= 25
		quarter += 1
	elif change >= 10:
		change -= 10
		dime += 1
	elif change >= 5:
		change -= 5
		nickle += 1
	elif change >= 1:
		change -= 1
		penny += 1
	else:
		keepGoing = False


print("\nChange: {}".format(changeOut))
print("\nTwenties: {}".format(twenty))
print("Tens: {}".format(ten))
print("Fives: {}".format(five))
print("Ones: {}".format(one))
print("Quarters: {}".format(quarter))
print("Dimes: {}".format(dime))
print("Nickles: {}".format(nickle))
print("Pennies: {}\n".format(penny))















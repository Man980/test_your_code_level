<<<<<<< HEAD
# this program is a game 
# it is so simple. Here is how it works:
# The computer will choose a random WORD from a list and you(user) will try to guess that word
# To guess the word chosen, you have multiple asterix equal to the amount of letters displayed on the screeen
#You job is to type letter by letter the word you are trying to guess
#Note that program needs to improve so your contributions are welcome.

import os
import random

dictionary = {'jovenel':'He is the most recent haitian president murdered.', 'ball':'It is a something rounded that people use to play football with'}

# storing dict keys in a list
key = []
for x in dictionary:
	key.append(x)

# the choice of the random word
name = random.choice(key)


length =int(len(name))
asterix = '*'*length

while name != asterix:
	os.system('cls')

	print(dictionary[name])
	print("\nThis the word you are trying to guess: ",asterix)
	
	a =input("Fill the asterix with missing letters:\n>>> ")
	a = a.lower()
	count = name.count(a)

	position = [pos for pos, char in enumerate(name) if char==a]

	if a in name and len(a)==1:

		if count==2:
			position = [pos for pos, char in enumerate(name) if char==a]

			position1 = position[0]
			position2 = position[1]

			asterix = asterix[:position1] +a+ asterix[position1+1:]
			asterix = asterix[:position2] +a+ asterix[position2+1:]

		elif count>2:
			position1 = position[0]
			position2 = position[1]
			position3 = position[2]

			asterix = asterix[:position1] +a+ asterix[position1+1:]
			asterix = asterix[:position2] +a+ asterix[position2+1:]
			asterix = asterix[:position3] +a+ asterix[position3+1:]
		else:
			position1 = position[0]
			asterix = asterix[:position1] +a+ asterix[position1+1:]

print(asterix)
	
=======
#this is a python project
>>>>>>> e85221269015fbfd6ec41c2d54463693098adc28

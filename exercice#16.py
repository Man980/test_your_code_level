#Exercice 16

import string
str_asccii = string.ascii_letters

split_string = "14P >1A <1V <1H >4O".split()
lis=[]

for elem in split_string:
	if elem[0] ==">":
		# recover the letter's position in ascii_letters 
		# and we add the letter's position +the the amount of steps to make
		#which is in elem
		position = str_asccii.index(elem[-1]) + int(elem[1:-1])

		element = str_asccii[position] # recover the letter hidden (grace to its position related to ascii letter + the amount of steps to make) 

		lis.append(element) #Add letters in list


	if elem[0] =="<":

		position = str_asccii.index(elem[-1]) - int(elem[1:-1])
		element = str_asccii[position]

		lis.append(element)

print(" ".join(lis))

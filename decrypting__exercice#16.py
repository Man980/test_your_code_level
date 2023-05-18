#Exercice 16
#You are given a tring like this you are try yo figure out what is it exactly

#INPUT and OUTPUT
#input : "<1T >7H >3C <5Y >13J <2C <5W >4A" ==> (output): "SOFTWARE"

#input : ">3A >0A <1U <10K >1A <9J <0S <16U" ==> (output): "DATABASE"

import string
str_asccii = string.ascii_letters

#UNCOMMENT TO TRY

#strs = "14P >1A <1V <1H >4O"
#strs = "<1T >7H >3C <5Y >13J <2C <5W >4A"

def decrypting(encrypted_message):
	split_string = encrypted_message.split()

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

decrypting(strs)

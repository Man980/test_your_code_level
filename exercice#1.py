#Don't forget to put in comment the other exercices when executing 

#Exercice 1
#ip = input("Enter you IP address\n>>> ")
ip =input('Enter your IP address. egz: 192.168.192')
ip = ip.replace('.','')
first_letter = int(ip[0])
add =0
for x in ip:
	add +=int(x)
print(add*first_letter)
#This function capitalizes the first letter of each word. It just takes a name as parameter
#Exercice 3

def camelcase(name):
	new_name = ''
	for x in name.lower().split():
		new_name+=x.capitalize()+' '
	print(new_name)

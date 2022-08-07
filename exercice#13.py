
#Exercice 13

#Exercice 14

#You have these input and output, give the combinations:

#a = 2                 4
#b = 16         

#a = 3                 4
#b = 24

#a = 1                 0.5
#b = 1

def in_out(a, b):
	if a== 2 and b ==16:
		print(int(b/(a*a)))

	elif a == 3 and b==24:
		print(int(b/(a*2)))

	elif a == 1 and b ==1:
		print(a/(a+b))

in_out(3, 24)
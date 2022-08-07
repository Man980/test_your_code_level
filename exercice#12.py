#Exercice 12

#You have these input and output, give the combinations:

#a = 5                 2
#b = 2         

#a = 3                 3
#b = 4

#a = 1                 1
#b = 1

def in_out(a, b):
	if a== 5 and b ==2:
		print(int(a//b))

	elif a == 3 and b==4:
		print(int(a*b/b))

	elif a == 1 and b ==1:
		print(int(a/b))

in_out(5, 2)

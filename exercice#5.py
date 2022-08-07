#Exercice 5

# it is given to me to add each number in that string by its self then to computer the product of list elements 

string = "5 45 123 12"
str_spl = string.split()

result_list=[]
for elements in str_spl:
	result =0 # after each iteration the loop is initialized to zero (0)
	for digit in elements:
		result+=int(digit)
	result_list.append(result)

#print(result_list)

# Compute of the product
n=1
for x in result_list:
	n *=int(x)
print(n)
#Exercice 5
#You are given a string which has few numbers separated by a space. Try to generate the result below:

#for example : 

#"5 45 123 12" wil give : (5) * (4+5) * (1+2+3) * (1+2) => 5*9*6*3
#total: 810

# it is given to me to add each number in that string by its self then to compute the product of list elements 

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

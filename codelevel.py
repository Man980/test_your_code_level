

#Don't forget to put in comment the other exercices when executing 

#Exercice 1
'''
#ip = input("Enter you IP address\n>>> ")
ip =input('Enter your IP address. egz: 192.168.192')
ip = ip.replace('.','')
first_letter = int(ip[0])
add =0
for x in ip:
	add +=int(x)
print(add*first_letter)
'''
'''
#Exercice 2
#As it is so simple, it is something made for beginners in a challenge
integer= int(input('Enter an enteger:\n>>> '))
if integer % 4 != 0:
	print('OK')
else:
	print('NOK')
'''


#This function capitalizes the first letter of each word. It just takes a name as parameter
#Exercice 3

'''
def camelcase(name):
	new_name = ''
	for x in name.lower().split():
		new_name+=x.capitalize()+' '
	print(new_name)
'''
'''
# Read carrefully the output bellow and comme back to read from the top and you will understand what it is meant for.
#Exercice 4
a = 2
b = 3
number =[2, 4, 5, 8, 9, 12, 15, 18]
ad0 =0
ad1=0
ad2 =0
ad3=0
lis0=[]
lis1=[]
lis2=[]
lis3=[]
for x in number:
	if x%a==0 and x%b != 0:
		lis0.append(x)
		ad0 +=x
	if x%b==0 and x%a !=0:
		lis0.append(x)
		ad1 +=x
	if x%b==0 and x%a ==0:
		lis2.append(x)
		ad2 +=x
	if x%b!=0 and x%a!=0:
		lis3.append(x)
		ad3 +=x
#Multiple of a not b
b = ''
for x in lis0:
	b += str(x)+' '
c = ''
for x in lis1:
	c += str(x)+' '
d = ''
for x in lis2:
	d += str(x)+ ' '
e = ''
for x in lis3:
	e += str(x)+' '
print(f'Numbers multiple of a not b are: {b} ==>', len(lis0))
print(f'Numbers multiple of b not a are: {c} ==>', len(lis1))
print(f'Numbers multiple of a and b are: {d} ==>', len(lis2))
print(f'Numbers that are neither multiple of a nor b are: {e} ==>', len(lis3))
'''
#Exercice 5
'''
# it is given to me to add each number in that string by its self then to computer the product of list elements 

string = "5 45 123 12"
str_spl = string.split()

result_list=[]
for elements in str_spl:
	result =0 # after each iteration the loop is initialized to zero (0)
	for digit in elements:
		result+=int(digit)
	result_list.append(result)

print(result_list)

# Compute of the product
n=1
for x in result_list:
	n *=int(x)
print(n)
'''
#Exercice 6

# this function allows you to reverse all carateres in a string (Slicing)
'''
def string_reverse(string):
	print(string[::-1])
string_reverse('Hello')
'''

#Exercie 7

string = 'je suis un haiti'
str_spl = string.split()
vowels =['a', 'e', 'i', 'o', 'u','y']
lis =[]

for chars in str_spl:
	for i in chars:
		if i in vowels:
			chars = chars.replace(chars[chars.index(i)-1], '*')
	lis.append(chars)
#print(" ".join(lis))
			

'''
#Exercice 8
def remove_space(string):
	newstr = string.replace(' ','')
	return newstr
print(remove_space('je le suis bien'))
'''
#Exercie 9

'''
# print all even numbers 
int_list = [1, 3, 4, 6, 8]
for x in int_list:
	if x %2==0:
		print(x)
'''
#Exercice 10
string = "web-insecure;34829sjdfnsj32984madsdkj"
string_new = string.split(';')
string_new.remove(string_new[0])
#print("".join(string_new))

'''
#Exercice 11
# That's a method used to display the largest and the smallest number
int_list =[1, 5, 0, -3, -4, 9]
new_list = sorted(int_list)
print(new_list[0], new_list[len(int_list)-1])
'''



#Exercice 12

#You have these input and output, give the combinations:

#a = 5                 2
#b = 2         

#a = 3                 3
#b = 4

#a = 1                 1
#b = 1
'''		
def in_out(a, b):
	if a== 5 and b ==2:
		print(int(a//b))

	elif a == 3 and b==4:
		print(int(a*b/b))

	elif a == 1 and b ==1:
		print(int(a/b))

in_out(5, 2)
'''
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

#in_out(3, 24)

#Exercie 15

#you have a string between two words "hidden" and "endpass", print out this string
text1 = " I'm hidden patagtou teolito endpass you hear me"
x = text1.split()
position1 = x.index('hidden')
position2 = x.index('endpass')

chars = x[position1+1:position2]
#print(" ".join(chars))

#Exercice 16
import string
#Men kèk done (INPUT) ak repons yo (OUTPUT):
str_asccii = string.ascii_letters

    #ap bay "PYTHON"
    #"14P <1V <1H >4O" 
    #ap bay "BUGS"
charact = ">5K <0Y <3W <3K <6U <3Q"
spl_charact = charact.split()
'''
str_digit=0
lis=[]
for elem in spl_charact:
	element =''
	for char in elem:
		if char in str_asccii:
			posi = str_asccii.index(char)
			print(posi)

	for el in elem:
		if el.isdigit():
			str_digit +=int(el)
		#element = str_asccii[posi-str_digit]
	
	if ">" in elem:
		element = str_asccii[posi+int(str_digit)]
		lis.append(element)
	if "<" in elem:
		elemen = str_asccii[posi-int(str_digit)]
		lis.append(elemen)
	'''

split_string = ">3A >0A <1U <10K >1A <9J <0S <16U".split()
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

# display duplicate numbers
def duplicateNumbers(nums):
	nums.sort()
	for i in range(1, len(nums)):
		if nums[i]==nums[i-1]:
			return nums[i]
print(duplicateNumbers([1, 4, 3, 5, 3, 4, 3,7]))



#preparing new challenges

# This line is only to test if my git terminal is working


def addIndexNumbers(_list):
	som = 0
	for i, x in enumerate(_list):
		som +=i
	print(som)

addIndexNumbers([1, 2, 3, 4 ])

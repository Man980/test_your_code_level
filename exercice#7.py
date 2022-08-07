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
print(" ".join(lis))
			
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
print(f'Numbers multiple of a not b are: {" ".join(b)} ==>', len(lis0))
print(f'Numbers multiple of b not a are: {" ".join(c)} ==>', len(lis1))
print(f'Numbers multiple of a and b are: {" ".join(d)} ==>', len(lis2))
print(f'Numbers that are neither multiple of a nor b are: {"".join(e)} ==>', len(lis3))
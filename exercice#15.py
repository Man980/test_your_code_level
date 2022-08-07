#Exercie 15

#you have a string between two words "hidden" and "endpass", print out this string
text1 = " I'm hidden patagtou teolito endpass you hear me"
x = text1.split()
position1 = x.index('hidden')
position2 = x.index('endpass')

chars = x[position1+1:position2]
#print(" ".join(chars))

#This app aims at generating the number of the open door among several

#for example:

#"127.0.0.1" will give you
#(1+2+7+0+0+1) * 1 = 11 => So the door that is opened is the door number 11

#ip = input("Enter your IP address\n>>> ")
ip =input('Enter your IP address. egz: 192.168.192\n>>>')
ip = ip.replace('.','')
first_digit = int(ip[0])
add =0
for x in ip:
	add +=int(x)
print(add*first_digit)

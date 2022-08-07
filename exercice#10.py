#that code remove all caracteres after the semi colon
#Exercice 10
string = "web-insecure;34829sjdfnsj32984madsdkj"
string_new = string.split(';')
string_new.remove(string_new[0])

print("".join(string_new))
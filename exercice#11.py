#Exercice 11
# That's a method used to display the largest and the smallest number wihout using the built-in functions MIN AND MAX
int_list =[1, 5, 0, -3, -4, 9]
new_list = sorted(int_list)
print(new_list[0], ",", new_list[len(int_list)-1])

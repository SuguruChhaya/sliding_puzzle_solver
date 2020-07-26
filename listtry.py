a = 1
b = 2
c = None
my_list = [a, b, c]
#*I cannot change a variable and a list itself in one step.
a= 3
my_list[2] = 4
print(my_list)
print(a)
print(c)
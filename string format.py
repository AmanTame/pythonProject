Firstname = "Aman"
Lastname = "Tame"

#print("My name is {} my father name is:{}".format(Firstname,Lastname))
#text="My name is {} and my father name is {}"
#print(text.format("Aman","Tame"))#positional argument

print("My name is {a} my father name is:{b}".format(a="Aman",b="Tame"))#keyword argument
print("My name is {0} my father name is:{1}".format("Aman","Tame"))#positional argument

name = "Aman"
print("My name is {:10} Nice to meet you!".format(name))
print("My name is {:>10} Nice to meet you!".format(name))
print("My name is {:^10} Nice to meet you!".format(name))

pi = 3.14159
print("The no pi is:{:.2f}".format(pi))
n = 1000
print("The no is:{:,}".format(n))
print("The no is:{:b}".format(n))
print("The no is:{:x}".format(n))
print("The no is:{:E}".format(n))


def add(a, b):
    return a+b
def sub(a, b):
    return a-b
def mult(a, b):
    return a*b
def div(a, b):
    return a/b
print("1.Sum")
print("2.Subtract")
print("3.Product")
print("4.Division")
s = int(input("Choose 1,2,3,4\n"))
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
if s == 1:
    z = add(x, y)
    print("The sum is: "+str(z))
elif s == 2:
    z = sub(x, y)
    print("The diff is: " + str(z))
elif s == 3:
    z = mult(x, y)
    print("The diff is: " + str(z))
elif s == 4:
    z = div(x, y)
    print("The diff is: " + str(z))

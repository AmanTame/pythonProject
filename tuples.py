#tuples contain  ordered and unchangeable data
#you can use duplicate data
student = ("Aman", "21", "male")

print(student.count("Aman"))
print(student.index("Aman"))

for i in student:
    print(i," ",end="")

if "Aman" in student:
    print("Aman is here!")

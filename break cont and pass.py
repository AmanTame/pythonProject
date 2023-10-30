name = input("enter your name")
while True:
    print(name)
    if name=="" or name !="":
        break

phone_number="251-123-456-789"
for i in phone_number:
    if i=="-":
        continue
    print(i,end="")
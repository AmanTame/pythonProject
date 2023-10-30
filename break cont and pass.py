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
for i in range(1,10):
    if i==5:
        pass
    else:
        print(i,end="")
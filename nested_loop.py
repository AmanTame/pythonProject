#nested loop
rows=int(input("Enter no of rows?"))
columns=int(input("Enter no of columns?"))
symbol=input("Enter symbol")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()

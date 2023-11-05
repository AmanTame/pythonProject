import random

x = random.randint(1,6) #displays random no b/n 0 and 6
y = random.random()   # displays random no b/n 0and 1
myList = ["A", "B", "C"]
print(x)
print(y)
z = random.choice(myList)
print(z)
cards = [1, 2, 3, 4, 5, "A", "Q", "Z"]
random.shuffle(cards)
print(cards)

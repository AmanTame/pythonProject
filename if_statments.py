age = int(input("How old are you?: "))
if age == 100:
    print("your are a century old!")
elif age >= 18:
    print("You are an adult!")
elif age <= 0:
    print("You are not born yet!")
else:
    print("You are a child!")

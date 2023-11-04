#accepts different no of arguments

def hello(**kwargs):
    print("Hello", end="")
    for key, value in kwargs.items():
        print(value, end="")
print(hello(Title="Mr.",First="Aman",middle="Tame"))


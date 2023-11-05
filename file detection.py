import os

path = "C:\\Users\\Dell\\Desktop\\class 1.txt"
if os.path.exists(path):
    print("the file exists!")
    if os.path.isfile(path):
        print("That is the file!")
    elif os.path.isdir(path):
        print("That is the directory!")
else:
    print("The file does not exist!")
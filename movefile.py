import os
source = "C:\\Users\\Dell\\Desktop\\r.txt"
destination = "C:\\Users\\Dell\\Desktop\\folder\\r.txt"
try:
    if os.path.exists(destination):
        print("Te file already exist!")
    else:
        os.replace(source, destination)
        print("The "+source+" is moved!")
except FileNotFoundError:
    print("The file not found!")

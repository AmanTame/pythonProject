try:
    with open("C:\\Users\\Dell\\Desktop\\cv.txt ") as file:
         print(file.read())
except FileNotFoundError:
    print("File not found!")


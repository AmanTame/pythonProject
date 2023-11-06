import os
import shutil
path = "C:\\Users\\Dell\\Desktop\\r.txt"
try:
    os.remove(path)  # delete a file
    os.rmdir(path)   # delete empty directory
    shutil.rmtree(path)  # delete a directory containing files



except FileNotFoundError:
    print("file not found")
except PermissionError:
    print("you dont hv permission!")
except OSError:
    print("You can not delete this file!")
else:
    print(path+" was deleted!")

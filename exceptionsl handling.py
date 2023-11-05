try:
    x = int(input("Enter no1:"))
    y = int(input("Enter no2:"))
    z = x / y

except ZeroDivisionError:
    print("you cant divide a no to zero")
except ValueError as e:
    #print(e)
    print("enter only numbers!")
except Exception:
    print("Something went wrong")
else:
    print(int(z))
finally:
    print("This always runs!")

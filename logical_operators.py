# logical operators and , or ,not
temp = int(input("what is the temperature outside?"))
if temp >= 0 and temp<= 30:
    print("the temperature is good! go outside")
elif temp < 0 or temp > 30:
    print("the temperature is bad! stay inside!")
# add 'not' by surrounding ( ) to the conditional statement to negate the value
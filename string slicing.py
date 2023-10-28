name = "Aman Tame"
firstname = name[0:3]
print(firstname)
last_name = name[5:]
print(last_name)
funky_name=name[0:9:2]  # the first "0" is starting point the
                        # second "9" is the end point
                        # the third is the steps of letter
a=name[::2] # space is not counted   :: refers from 0 to the very end of the string
print(funky_name)
print(a)
reverse_name = name[::-1]
print(reverse_name)

# slice function
website = "https://www.google.com"
website2 = "https://www.wikipedia.com"
sliced_piece = slice(12, -4)
print(website[sliced_piece])
print(website2[sliced_piece])

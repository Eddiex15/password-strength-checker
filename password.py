import re

password = input("enter your password")
if len(password)<8:
    print("password must be atleast 8 charcters long.")
    elif not re.search("[A-Z]", password):
        print("password must contain one uppercase")
     elif not re.search("[a-z]", password):
        print("password must contain one lowercase")
    elif not re.search("[0-9]", password):
        print("password must contain one number")

        else:
            print("password is strong")
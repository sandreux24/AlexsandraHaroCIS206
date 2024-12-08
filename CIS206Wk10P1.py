import re

s=input("Enter a string to test: ")

def checkValidString(s):
    pattern = "^[a-zA-Z0-9]+$"
    if re.match(pattern, s):
        print(f"Valid string")

    else:
        print(f"Invalid string")


checkValidString(s)

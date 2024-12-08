import re

s = input("Enter a string to test for this pattern: ")

def matchWordAtBeginning(s):
    pattern = r"^\w+"
    match = re.match(pattern, s)
    if match:
        print(f"Word at the beginning: {match.group()}")
    else:
        print(f"'{s}' does not match the pattern ")

matchWordAtBeginning(s)

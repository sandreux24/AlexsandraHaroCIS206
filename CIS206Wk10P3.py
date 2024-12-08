import re

s = input("Enter a string to test for this pattern: ")

def matchAfollowedByMultipleB(s):
    pattern = "^ab+$"
    if re.match (pattern, s):
        print(f"'{s}' matches the pattern")
    else:
        print(f"'{s}' does not match the pattern ")

matchAfollowedByMultipleB(s)

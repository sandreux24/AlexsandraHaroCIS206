import re

s = input("Enter a string to test for this pattern: ")

def matchAfollowedByB(s):
    pattern = "^ab*$"
    if re.match (pattern, s):
        print(f"'{s}' matches the pattern")
    else:
        print(f"'{s}' does not match the pattern ")

matchAfollowedByB(s)

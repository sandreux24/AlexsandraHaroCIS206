import re

s = input("Enter a string to test for this pattern: ")

def findLowercasewithUnderscore(s):
    pattern = "^[a-z]+(?:_[a-z]+)*$"
    if re.match (pattern, s):
        print(f"'{s}' matches the pattern")
    else:
        print(f"'{s}' does not match the pattern ")

findLowercasewithUnderscore(s)

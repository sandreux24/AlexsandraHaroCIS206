import re

s = input("Enter a string to test for this pattern: ")

def removeLeadingZero(s):
    pattern = r"\b0*(\d+)\b"
    result = re.sub(pattern, r"\1", s)
    print(f"IP address without leading zeros: {result}")

removeLeadingZero(s)

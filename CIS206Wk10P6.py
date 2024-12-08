import re

s = input("Enter a string to test for this pattern: ")

def containingZ(s):
    pattern = r"\b\w*z\w*\b"
    match = re.findall(pattern, s)
    if match:
        print(f"Words containing 'z': {match}")
    else:
        print(f"'{s}' does not contain 'z' ")

containingZ(s)

"""The quick brown fox jumps over the lazy dog.
Python Exercises."""

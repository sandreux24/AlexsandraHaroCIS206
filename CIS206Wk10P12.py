import re

text = input("Enter the text that will look for words that begin with 'a' and 'e': ")

def lookingForAandE (text):
    pattern = r"\b[aeAE]\w*\b"
    words = re.findall(pattern, text)
    if words:
        print (f"Words starting with 'a' and 'e': {words}")

    else:
        print(f"Theres no words that begin with 'a' or 'e'.")


lookingForAandE(text)

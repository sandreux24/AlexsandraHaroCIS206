import re

text = input("Enter the text thats going to be modified.")

def replaceWithColon(text):
    modifyText = re.sub(r"[ ,.]", ":", text)
    return modifyText

result = replaceWithColon(text)
print("Modified string: ", result)

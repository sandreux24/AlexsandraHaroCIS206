import re

text = input("Enter the text to remove extra spaces: ")

def removeExtraSpaces(text):
    modifyText = re.sub(r'\s+', ' ', text).strip()
    return modifyText

result = removeExtraSpaces(text)
print(f"Modified text: {result}")


"""The   following example creates an ArrayList with a    capacity of 50 elements.  Four   elements are           then added to the ArrayList and the ArrayList is trimmed             accordingly."""

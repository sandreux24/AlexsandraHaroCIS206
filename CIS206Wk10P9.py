import re

words = input("Enter the word(s) youre looking for(separate by commas): ").split(',')
text = input("Enter the text to look for the word: ")

def searchAndLocation(text, words):
    for word in words:
        word = word.strip()
        match = re.search(rf"\b{re.escape(word)}\b", text)
        if match:
            print(f"'{words}' found at location {match.start()}")
        else :
            print(f"'{words}' not found in the text.")   
    

searchAndLocation(text, words)

import re

words = input("Enter the word(s) youre looking for(separate by commas): ").split(',')
text = input("Enter the text to look for the word: ")

def stringSearch(text, words):
    for word in words:
        word = word.strip()
        if re.search(rf"\b{re.escape(word)}\b", text):
            print(f"'{word}' found in text.")
        else :
            print(f"'{word}' not found in the text.")   
    

stringSearch(text, words)


import re

text = input("Enter text to replace whitespaces with underscores: ")

def replaceSpaces(text):
    textWithUnderscores = re.sub(r"\s", "_", text)
    textWithSpaces = re.sub(r"_", " ", text)

    print(f"Text with underscores: {textWithUnderscores}")
    print(f"Text with spaces: {textWithSpaces}")

replaceSpaces(text)

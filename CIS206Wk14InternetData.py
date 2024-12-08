import json


with open('books.json', 'r') as file:
    booksData = json.load(file)

def searchBook (title):
    for book in booksData:
        if book['title'].lower() == title.lower():
            return book
    return None

print(f"Books Data: ")
for book in booksData:
    print(f"Title: {book['title']}, Author:{book['author']}, Year {book['year']}")
print("\n")

while True:
    searchTitle = input("Enter a book title to search or type 'quit' to exit: ")
    
    if searchTitle.lower() == 'quit':
        print(f"Exiting program.")
        break

    foundBook = searchBook(searchTitle)
    if foundBook:
        print(f"Book has been found. Title: {foundBook['title']}, Author: {foundBook['author']}, Year: {foundBook['year']}  ")

    else:
        print(f"Title '{searchTitle}' not found.")        


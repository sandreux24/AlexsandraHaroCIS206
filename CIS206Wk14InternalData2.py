import xml.etree.ElementTree as ET


tree = ET.parse('books.xml')
root = tree.getroot()


def searchBook(title):
    for book in root.findall('book'):
        bookTitle = book.find('title').text
        if bookTitle.lower() == title.lower():
            author = book.find('author').text
            year = book.find('year').text
            return {'title': bookTitle, 'author': author, 'year': year}
    return None


print("Books Data:")
for book in root.findall('book'):
    title = book.find('title').text
    author = book.find('author').text
    year = book.find('year').text
    print(f"Title: {title}, Author: {author}, Year: {year}")
print("\n")


while True:
    searchTitle = input("Enter a book title to search for (or type 'quit' to exit): ")
    if searchTitle.lower() == 'quit':
        break
    foundBook = searchBook(searchTitle)
    if foundBook:
        print(f"Found! Title: {foundBook['title']}, Author: {foundBook['author']}, Year: {foundBook['year']}")
    else:
        print(f"Title '{searchTitle}' not found.")

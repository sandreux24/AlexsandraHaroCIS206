import re

url = input("Enter a URL to find date: ")

def exactDateFromURL(url):
    pattern = r"/(\d{4})/(\d{2})/(\d{2})/"

    match = re.search(pattern, url)
    if match:
        year, month, day = match.groups()
        print (f"Year: {year}, Month: {month}, Day: {day}")

    else:
        print(f"No date found in the URL. ")

exactDateFromURL(url)    

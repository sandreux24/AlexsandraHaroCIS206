def loadNames(filename):
    try:
        with open(filename, 'r') as file:
            names = [line.strip() for line in file.readlines()]
        return names
    except IOError:
        print(f"Error: The file {filename} was not been found.")
        return[]
    
def searchAndLogName(names, nameToSearch, outputFile):
    if nameToSearch in names:
        print(f"Name '{nameToSearch}' has been found in the file.")

    else:
        print(f"Name '{nameToSearch}' was not found in file. Noting name in {outputFile}.")
        with open(outputFile, 'a') as file:
            file.write(nameToSearch + '\n')    
def main ():
    names = loadNames("names.txt")

    if not names:
        print(f"No names have been found in the file or file could not load.")
        return
    
    outputFile = "notFoundNames.txt"

    while True:
        userInput = input(f"Enter a name or type exit to quit: ").strip()

        if userInput.lower() == 'exit':
            print(f"Program is now ending.")
            break

        searchAndLogName(names, userInput, outputFile)
if __name__ == "__main__":
    main()



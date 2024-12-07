import re

def runLength(inputString):
    if not inputString.isalpha():
        raise ValueError(f"Input should only be letters.")

    string = []
    count = 1
    length = len(inputString)

    for i in range(1, length + 1):
        if i < length and inputString[i] == inputString[i-1]:
            count += 1
        else: 
            if count > 1:
                string.append(f"{inputString[i-1]}{count}")
            else:
                string.append(inputString[i-1])
                
            count =1 
                        
    return "".join(string)
        
def decode(encodedString):

    if not re.match(r'^[A-Za-z0-9]*$', encodedString):
        raise ValueError("Encoded String contain invalid characters.")
    
    decodedString = []
    i = 0 
    
    while i < len(encodedString):
        char = encodedString[i]
        i += 1
        count = 1

        if i < len(encodedString) and encodedString[i].isdigit():
            count = int(encodedString[i])
            i += 1

        decodedString.append(char * count)

    return "".join(decodedString)

def check4RLEformat(inputString):
    return bool(re.match(r'^[A-Za-z0-9]*$', inputString)) and bool(re.search(r'\d', inputString))
    
def main():
    userInput = input(f"Enter a string: ")

    #try:
    #    rleResult = runLength(userInput)
    #    print (f"Run Length Encoded string: {rleResult}")
    #except ValueError as e:
    #    print(e)

    try:
        if check4RLEformat(userInput):
            decodedString = decode(userInput)
            print(f"Decoded string: {decodedString}")
        else:
            encodedString = runLength(userInput)
            print(f"Encoded String: {encodedString}")
    
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()





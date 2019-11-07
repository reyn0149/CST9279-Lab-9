userInput = input("What is the name of your .csv file?")

with open(userInput, 'r') as userFile:
        stripped = (line.strip() for line in userFile)
        lines = (line.split(",") for line in stripped if line)
        printedList =list(lines)
        print(printedList)
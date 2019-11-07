import csv

def convertToCsv(fileName):
    originalFile = (fileName + ".txt")
    convertedFile = (fileName + ".csv")
    with open(originalFile, 'r') as inputFile:
        stripped = (line.strip() for line in inputFile)
        lines = (line.split(",") for line in stripped if line)
        with open(convertedFile, 'w') as outputFile:
            writer = csv.writer(outputFile)
            writer.writerow(('First Name', 'Count'))
            writer.writerows(lines)

convertToCsv("2000_BoysNames")
convertToCsv("2000_GirlsNames")
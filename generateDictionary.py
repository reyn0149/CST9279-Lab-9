from gfxhat import lcd, fonts
from PIL import Image, ImageFont, ImageDraw
from click import getchar

xCoordinate = 64
yCoordinate = 32
userInput = 0

def generateDictionary():
    outputDictionary = {}
    with open ('font3.txt', 'r') as dictionaryFile:
        for line in dictionaryFile:
            value, key = line.strip().split(',')
            outputDictionary[key.strip()] =value.strip()
    return(outputDictionary)
    
def clearScreen(lcd):
    lcd.clear()
    lcd.show()
    
dictionary = generateDictionary()

userInput = getchar()
print(userInput)

if userInput in dictionary:
    objectHex = list(dictionary[userInput])
    print objectHex
    clearScreen(lcd)
    row =[]
    y = 5
    i = 2
    while i < 17:
        hexChunk = objectHex[i] + objectHex[i+1]
        objectBinary = list(bin(int(hexChunk,16))[2:].zfill(8))
        print objectBinary
        for x in range (len(objectBinary)):
            
            lcd.set_pixel(5+x,y,int(objectBinary[x]))
            lcd.show()
        i = i+2
        y = y+1
        
else:
	print("Sorry! That value isn't in my dictionary!")

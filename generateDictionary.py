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

def displayText(text,lcd,x,y):
    lcd.clear()
    width, height = lcd.dimensions()
    image = Image.new('P', (width, height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fonts.AmaticSCBold, 12)
    w, h = font.getsize(text)
    draw.text((x,y), text, 1, font)
    for x1 in range(x,x+w):
        for y1 in range(y,y+h):
            pixel = image.getpixel((x1, y1))
            lcd.set_pixel(x1, y1, pixel)
    lcd.show()
    
dictionary = generateDictionary()
displayText("Welcome! Press a key!",lcd,2,3)

userInput = getchar()
print(userInput)
if userInput in dictionary:
	clearScreen(lcd)
	displayText(userInput,lcd,2,2)
else:
	print("Sorry! That value isn't in my dictionary!")

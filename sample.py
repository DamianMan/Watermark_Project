
from PIL import Image, ImageFont, ImageDraw
#---------------- HOW TO IMPORT AN IMAGE AND DRAW A TEXT ON IT -------------------#
img = Image.open('car.jpeg')
img.resize((200,200))
draw = ImageDraw.Draw(img)

# Get a "Chalkduster" TTF
chalk = ImageFont.truetype("Chalkduster.ttf",16)

# Get a "Keyboard" TTF
kbd = ImageFont.truetype("Keyboard.ttf",26)

# Make example for Lazy One - showing how to colour cyan too
draw.text((300,400),"Keyboard",font=kbd, fill="#00ff00")

# And another
draw.text((300,240),"Chalkduster",font=chalk)
img.save("test.png")

img.show()
#to allow program use images
from PIL import Image
#to allow program calculate mode
from statistics import mode
#to read image
img=(r"C:\Users\Dabira.Akinwande\Downloads\image.jpeg")
#to open image
image = Image.open(img)
#to convert image to rgb format
image_to_rgb = image.convert('RGB')
#to get image size
width, height = image.size
#a list to store the pixels
pixel = []
for x in range(width):
    for y in range(height):
        r, g, b = image_to_rgb.getpixel((x, y))
        pixel.append((r, g, b))
#to calculate the mode of the pixels
mode_pixels = mode(pixel)
#to give new colour choices
print('''Red is 255,0,0
        Black is 0,0,0
        White is 255,255,255
        Blue is 0,0,255
        Yellow is 255,255,0
        Green is 0,128,0
        Purple is 128,0,128
        Grey is 128,128,128
        Orange is 255,165,0
        Pink is 255,105,180
      ''')

colours=input("Enter the colour code for your desired new colour:")
colour=tuple(map(int, colours.split(',')))
for x in range(width):
    for y in range(height):
        r, g, b = image_to_rgb.getpixel((x, y))
        #to replace background colour
        if(r, g, b) == mode_pixels:
            image_to_rgb.putpixel((x,y), colour)
#to show the image
image_to_rgb.show()
#to save image
image_to_rgb.save('New pic.jpeg')

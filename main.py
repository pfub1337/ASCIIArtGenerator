from PIL import Image, ImageDraw, ImageFont
import math
import os
import time

# CFG Loading

defaultValues = {"chars": "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. ",
                 "scaleMultiply": "0.2",
                 "charWidth": "10",
                 "charHeight": "20",
                 "fontPath": "C:\\Windows\\Fonts\\Consola.ttf",
                 "fontSize": "20",
                 "imgName": "source.jpg"}

values = {"chars": "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. ",
          "scaleMultiply": "0.2",
          "charWidth": "10",
          "charHeight": "20",
          "fontPath": "C:\\Windows\\Fonts\\Consola.ttf",
          "fontSize": "20",
          "imgName": "source.jpg"}

with open("config.txt", "r") as f:
    for line in f.readlines():
        if line[0] != "#":
            val = line.split(" : ")
            try:
                values[val[0]] = val[1][:-1]
            except Exception as ex:
                print("Config file isn't configured correctly! Program will be closed.")
                print("Error:", ex)
                exit(0)
    print("Config was successfully installed!")

chars = str(values["chars"] + " ")[::-1]
scaleMultiply = float(values["scaleMultiply"])
interval = len(chars)/256
charWidth = int(values["charWidth"])
charHeight = int(values["charHeight"])
fontPath = values["fontPath"]
print(values["fontPath"])
fontSize = int(values["fontSize"])
font = ImageFont.truetype(fontPath, fontSize)
imgName = values["imgName"]

# Loading image

def getChar(inputInt):
    return chars[math.floor(inputInt * interval)]

img = Image.open(imgName)
width, height = img.size
img = img.resize((int(width * scaleMultiply), int(height * scaleMultiply * (charWidth / charHeight))), Image.NEAREST)
width, height = img.size
px = img.load()
ASCIIimg = Image.new("RGB", (width * charWidth, height * charHeight), (0, 0, 0))
imgDraw = ImageDraw.Draw(ASCIIimg)
file = open("Output.txt", "w")
tStart = int(time.time())

for i in range(height):
    tempT = int(time.time()) - tStart
    secT = tempT % 60
    minT = tempT // 60
    hourT = minT % 60
    for j in range(width):
        r, g, b = px[j, i]
        h = int((r + g + b) / 3)
        px[j, i] = (h, h, h)
        file.write(getChar(h))
        imgDraw.text((j * charWidth, i * charHeight), getChar(h), font=font, fill=(r, g, b))
    file.write("\n")
    os.system("cls" if os.name == "nt" else "clear")
    print(f"{round((i + 1) / height * 100, 1)}%\tTime: {hourT if hourT > 9 else '0' + str(hourT)}:{minT if minT > 9 else '0' + str(minT)}:{secT if secT > 9 else '0' + str(secT)}")
    print(f"[{'█' * int(round((i + 1) / height * 100, 0) // 10)}{'▒'* (10 - int(round((i + 1) / height * 100, 0) // 10))}]")

ASCIIimg.save("output.jpg")
file.close()
print("Text version of art is successfully saved as \"Output.txt\"\nPicture is saved as \"Output.jpg\"")
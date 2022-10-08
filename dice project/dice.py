from PIL import Image, ImageOps, ImageDraw


def diceImage(dicenumber, dicesize):
    dim = Image.open("dice/" + str(dicenumber) + ".jpg")
    dim = dim.resize((dicesize, dicesize), Image.ANTIALIAS)
    return dim


dice_width = 100

img = Image.open("1638625115116.jpg")
img = ImageOps.grayscale(img)
img = ImageOps.equalize(img)

dice_height = img.height / img.width * dice_width

dice_size = int(img.width / dice_width)

nim = Image.new("L", (img.width, img.height), 'white')
nimd = ImageDraw.Draw(nim)


print(img.width, img.height, dice_width, dice_height, dice_size)

print(f'Dice needed: {dice_width * int(dice_height)}')

for y in range(0, img.height, dice_size):
    for x in range(0, img.width, dice_size):
        thisSectorColor = 0
        for dicex in range(0, dice_size):
            for dicey in range(0, dice_size):
                thisSectorColor += img.getpixel((x + dicex, y + dicey))
        thisSectorColor = thisSectorColor / (dice_size ** 2)

        nimd.rectangle(((x, y), (x + dice_size, y + dice_size)), int(thisSectorColor))
        diceNumber = (255 - thisSectorColor) * 6 / 255 + 1
        print(int(diceNumber), end="")
        img.paste(diceImage(int(diceNumber), dice_size), (x, y))
    print("")
img.save("diceimage.png")
img.show()

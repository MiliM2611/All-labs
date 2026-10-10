from PIL import Image

img = Image.open("img1.jpg")

left = 200
top = 200
right = img.width - 200
bottom = img.height - 0

cropped = img.crop((left, top, right, bottom))
cropped.save("img1Cropped.jpg")
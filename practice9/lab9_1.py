from PIL import Image

image = Image.open('img.png')

print(f"Size: {image.size}")
print(f"Format: {image.format}")
print(f"Color: {image.mode}")

image.show()
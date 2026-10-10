from PIL import Image

img = Image.open("img.png")

new_width = img.width // 3
new_height = img.height // 3

resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

resized_img.save("imgResized.png")
img = Image.open("imgResized.png")

flipped_img = img.transpose(Image.FLIP_LEFT_RIGHT)
flipped_img.save('flippedHorizontal.png')

flipped_img = img.transpose(Image.FLIP_TOP_BOTTOM)
flipped_img.save('flippedVertical.png')

print("Изображения сохранены")

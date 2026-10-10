from PIL import Image, ImageDraw, ImageFont
import random

dict = {
    "Новый год": "postcards/newYear.jpg",
    "День рождения": "postcards/birthday.jpg",
    "День труб": "postcards/pipe.jpg"
}

print("Выберите праздник (введите номер):")
i = 1
for key in dict:
    print(f"{i}) " + key)
    i += 1

temp = input()
match temp:
    case "1":
        img = Image.open(dict["Новый год"])
    case "2":
        img = Image.open(dict["День рождения"])
    case "3":
        img = Image.open(dict["День труб"])

name = input("А поздравить кого хотите (в именительном падеже, пожалуйста)?\n")
draw = ImageDraw.Draw(img)

arial = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", size=50)
times = ImageFont.truetype("C:/Windows/Fonts/times.ttf", size=50)
impact = ImageFont.truetype("C:/Windows/Fonts/impact.ttf", size=50)
arialbd = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", size=50)
timesbd = ImageFont.truetype("C:/Windows/Fonts/timesbd.ttf", size=50)
font = random.choice([arial, times, impact, arialbd, timesbd])
color = random.choice(["white", "black", "red", "blue"])

width, height = img.size
x = width // 2 - 50
y = random.choice([50, height // 2 + 25, height - 150])

text = ", \nпоздравляю!"
draw.text((x, y), name + text, font=font, fill=color)

img.show()
img.save("postcard.png")
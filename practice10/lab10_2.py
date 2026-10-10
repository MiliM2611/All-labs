from PIL import Image

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
        img.show()
    case "2":
        img = Image.open(dict["День рождения"])
        img.show()
    case "3":
        img = Image.open(dict["День труб"])
        img.show()

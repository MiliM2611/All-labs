# 4.4) Цвета

colors = ["красный", "синий", "желтый"]
color1, color2 = map(str, input("Введите названия цветов через пробел с маленькой буквы: ").split())

if color1 not in colors or color2 not in colors:
    print("Неизвестные цвета")
else:
    if (color1 == colors[0] and color2 == colors[1]) or (color1 == colors[1] and color2 == colors[0]):
        print("Фиолетовый")
    elif (color1 == colors[0] and color2 == colors[2]) or (color1 == colors[2] and color2 == colors[0]):
        print("Оранжевый")
    elif (color1 == colors[1] and color2 == colors[2]) or (color1 == colors[2] and color2 == colors[1]):
        print("Зеленый")

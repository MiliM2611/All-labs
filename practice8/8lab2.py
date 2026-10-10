points = {
    1: "АВЕИНОРСТ",
    2: "ДКЛМПУ",
    3: "БГЁЬЯ",
    4: "ЙЫ",
    5: "ЖЗХЦЧ",
    8: "ШЭЮ",
    10: "ФЩЪ"
}

word = input("Введите слово: ").upper()

count = 0

for i in word:
    for point, letters in points.items():
        if i in letters:
            count += point
            break

print("Стоимость слова:", count)
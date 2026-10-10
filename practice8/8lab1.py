world = {
    "Россия": "Москва",
    "США": "Вашингтон",
    "Беларусь": "Минск",
    "Китай": "Пекин",   
    "Казахстан": "Астана",
    "Франция": "Париж",
    "Япония": "Токио"
}

for country, capital in world.items():
    print(country, "-", capital)

country = input("Введите страну: \n")

if country in world:
    print("Столица:", world[country])
else:
    print("Такой страны нет в словаре")

print("\nПо алфавиту:")

for country in sorted(world):
    print(country, "-", world[country])
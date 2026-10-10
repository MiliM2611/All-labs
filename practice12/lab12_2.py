import json

with open("products1.json", "r", encoding="utf-8") as file:
    data = json.load(file)

name = input("Введите название продукта: ")
price = int(input("Введите цену продукта: "))
weight = int(input("Введите вес продукта: "))
available = input("Продукт в наличии? (да/нет): ").strip().lower()
if available == "да":
    available = True 
else:
    available = False

newProduct = {
    "name": name,
    "price": price,
    "weight": weight,
    "available": available
}

data["products"].append(newProduct)

with open("products1.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

# Выводим все продукты на экран
for product in data["products"]:
    print(f"\nНазвание: {product['name']}")
    print(f"Цена: {product['price']}")
    print(f"Вес: {product['weight']}")
    if product["available"]:
        print("В наличии")
    else:
        print("Нет в наличии!")
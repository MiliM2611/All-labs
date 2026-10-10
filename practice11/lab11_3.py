import csv

total = 0

print("Нужно купить:")

with open("products.csv", encoding="utf-8") as file:
    reader = csv.reader(file)

    next(reader)

    for row in reader:
        product = row[0]
        count = int(row[1])
        price = int(row[2])

        total += count * price

        print(f"{product} - {count} шт. за {price} руб.")

print(f"\nИтоговая сумма: {total} руб.")
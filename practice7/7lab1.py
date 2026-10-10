numbers = [1, 12, 27, 79, 90]

n = int(input("Введите число: "))

print("Исходный список:", numbers)
print("Ваше число:", n)

if n in numbers:
    print("Поздравляю, Вы угадали число!")
else:
    print("Нет такого числа!")
# 5.4
import random
count = 0
countRight = 0
while count != 3:
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    sum = int(input(f"{a} + {b} = "))
    if sum == a + b:
        print("Правильно!")
        countRight += 1
    else:
        print("Ответ неверный")
        count += 1

print(f"Игра окончена. Правильных ответов: {countRight}")

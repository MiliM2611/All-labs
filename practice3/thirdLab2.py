# 3.2) Решение линейного уравнения

print("____ ax + b = c ____")
a, b, c = map(int, input("Введите 3 числа через пробел\n").split())
x = (c - b) / a
print(x)
# 6.2
def div100(num):
    if not num.isdigit():
        raise ValueError("Введена строка!")
    elif num == "0":
        raise ZeroDivisionError("Нельзя делить на 0")
    return 100 % int(num) == 0

a = str(input("Введите число: "))
if div100(a):
    print(f"100 делится на {a}")
else:
    print(f"100 не делится на {a}")
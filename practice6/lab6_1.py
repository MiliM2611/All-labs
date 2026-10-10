# 6.1
def div3(a):
    if a % 3 == 0:
        return True
    else:
        return False
a = int(input("Введите число: "))
if div3(a):
    print(f"Число {a} делится на 3")
else:
    print(f"Число {a} не делится на 3")
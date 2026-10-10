# 6.4
def happyNum(num):
    l = len(num)
    fir = 0
    sec = 0
    for i in range((l//2)):
        fir += int(num[i])
    for i in range((l//2), l):
        sec += int(num[i])
    return fir == sec

a = str(input("Введите номер билета с четным числом цифр: "))
if happyNum(a):
    print("У вас счастливый билет")
else:
    print("Ваш билет не счастливый")
# 5.3
print("Для завершения введите \"stop\"")
while True:
    word = str(input("Введите слово: "))
    if word == "stop":
        break
    if "ф" in word or "Ф" in word:
        print("Ого! Это редкое слово!")
    else:
        print("Эх, это не очень редкое слово...")
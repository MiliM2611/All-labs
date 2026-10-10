numbers = [1, 12, 27, 12, 79, 90, 1]

same = []

for n in numbers:
    if numbers.count(n) > 1 and n not in same:
        same.append(n)

if same:
    print("Повторяющиеся элементы:", *same)
else:
    print("Повторяющихся элементов нет")
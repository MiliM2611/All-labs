# 5.1

N = int(input("Введите кол-во слов: "))
print("Введите слова построчно")
words = ""

for i in range(N):
    words = words + str(input()) + " "

print(words)
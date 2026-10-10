# 5.2


print("Введите слова построчно")
words = ""
while True:
    word = str(input())
    if word == "stop":
        break
    words = words + word + " "

print(words)
with open("en-ru.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

dictionary = {}

for line in lines:
    parts = line.strip().split(" - ")

    if len(parts) != 2:
        continue

    english = parts[0].strip()
    russianWords = parts[1].split(", ")

    for russian in russianWords:
        russian = russian.strip()

        if russian not in dictionary:
            dictionary[russian] = []

        if english not in dictionary[russian]:
            dictionary[russian].append(english)

with open("ru-en.txt", "w", encoding="utf-8") as file:
    for russian in sorted(dictionary):
        english = ", ".join(dictionary[russian])
        file.write(f"{russian} – {english}\n")

students = {
    "Дмитрий": ["русский", "английский"],
    "Виктор": ["русский", "китайский"],
    "Николай": ["русский"],
    "Анна": ["русский", "японский"],
    "Михаил": ["английский", "немецкий"],
    "Ольга": ["русский", "китайский", "английский"]
}

languages = set()

for i in students:
    for language in students[i]:
        languages.add(language)

print("Количество различных языков:", len(languages))
print("Языки:", *sorted(languages))

print("Знают китайский:")
for i in students:
    if "китайский" in students[i]:
        print(i)
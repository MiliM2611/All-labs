import tkinter as tk
import urllib.request
import json

window = tk.Tk()
window.title("Информация о стране")
window.geometry("400x400")

title = tk.Label(
    window,
    text="Информация о стране",
    font=("Arial", 20)
)
title.pack(pady=20)

label = tk.Label(
    window,
    text="Введите код страны (например RU):"
)
label.pack()

entry = tk.Entry(window, width=20)
entry.pack(pady=10)

result = tk.Label(
    window,
    text="",
    font=("Arial", 12),
    justify="left"
)
result.pack(pady=30)


def findCountry():
    code = entry.get().upper()

    url = "https://countries.dev/alpha/" + code

    request = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0"}
    )

    response = urllib.request.urlopen(request)
    data = json.loads(response.read())

    result["text"] = (
        f"Страна: {data['name']}\n"
        f"Столица: {data['capital']}\n"
        f"Регион: {data['region']}\n"
        f"Население: {data['population']}"
    )


button = tk.Button(
    window,
    text="Найти",
    command=findCountry
)
button.pack(pady=10)

window.mainloop()
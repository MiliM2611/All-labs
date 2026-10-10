from tkinter import *
import requests

root = Tk()

def get_weather():
    city = cityField.get()

    key = "035844ffecd55c4fe5941a5045c8ce54"
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {"appid": key, "q": city, "units": "metric"}

    result = requests.get(url, params=params)
    weather = result.json()

    info["text"] = f"{weather['name']}: {weather['main']['temp']}°C"


root["bg"] = "#F7F2F8"
root.title("Погодное приложение")
root.geometry("360x280")
root.resizable(width=False, height=False)

frame_top = Frame(root, bg="#DCD6F7", bd=8, relief="flat")
frame_top.place(relx=0.08, rely=0.12, relwidth=0.84, relheight=0.35)

frame_bottom = Frame(root, bg="#E8DFF5", bd=8, relief="flat")
frame_bottom.place(relx=0.08, rely=0.60, relwidth=0.84, relheight=0.22)

cityField = Entry(
    frame_top,
    bg="#FFFFFF",
    fg="#514B64",
    font=("Segoe UI", 12),
    relief="flat",
    justify="center"
)
cityField.pack(pady=8, padx=10, fill="x")

btn = Button(
    frame_top,
    text="Посмотреть погоду",
    command=get_weather,
    bg="#B8C0FF",
    fg="#37334A",
    font=("Segoe UI", 10, "bold"),
    relief="flat",
    activebackground="#A5AEF5",
    activeforeground="#37334A",
    cursor="hand2"
)
btn.pack(pady=5, padx=10, fill="x")

info = Label(
    frame_bottom,
    text="Погода в городе",
    bg="#E8DFF5",
    fg="#514B64",
    font=("Segoe UI", 12, "bold"),
    wraplength=270
)
info.pack(expand=True)

root.mainloop()
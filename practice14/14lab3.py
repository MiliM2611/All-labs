import tkinter as tk


class IceCreamStand:
    def __init__(self, flavors):
        self.flavors = flavors

    def show_flavors(self):
        for flavor in self.flavors:
            listbox.insert(tk.END, flavor)


# Создаём кафе-мороженое
cafe = IceCreamStand([
    "Ванильное",
    "Шоколадное",
    "Клубничное",
    "Фисташковое",
    "Пломбир"
])


window = tk.Tk()
window.title("Кафе-мороженое")
window.geometry("400x400")

label = tk.Label(
    window,
    text="Кафе-мороженое",
    font=("Arial", 20)
)
label.pack(pady=20)

listbox = tk.Listbox(
    window,
    width=30,
    height=10
)
listbox.pack()

cafe.show_flavors()

button = tk.Button(
    window,
    text="Выбрать мороженое",
    command=lambda: print(listbox.get(listbox.curselection()))
)
button.pack(pady=20)

window.mainloop()
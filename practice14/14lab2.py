class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, rating):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = rating

    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)
        print("Рейтинг:", self.rating)

    def open_restaurant(self):
        print("Ресторан открыт")

    def update_rating(self, new_rating):
        self.rating = new_rating


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, rating, flavors, location, working_hours):
        super().__init__(restaurant_name, cuisine_type, rating)
        self.flavors = flavors
        self.location = location
        self.working_hours = working_hours

    # Вывод сортов мороженого
    def show_flavors(self):
        print("Сорта мороженого:")
        for flavor in self.flavors:
            print(flavor)

    # Добавление сорта
    def add_flavor(self, flavor):
        self.flavors.append(flavor)

    # Удаление сорта
    def remove_flavor(self, flavor):
        if flavor in self.flavors:
            self.flavors.remove(flavor)

    # Проверка наличия сорта
    def check_flavor(self, flavor):
        if flavor in self.flavors:
            print("Такое мороженое есть")
        else:
            print("Такого мороженого нет")

    # Мороженое на палочке
    def ice_cream_on_stick(self):
        print("Мороженое на палочке")

    # Мягкое мороженое
    def soft_ice_cream(self):
        print("Мягкое мороженое")

    # Мороженое в стаканчике
    def ice_cream_in_cup(self):
        print("Мороженое в стаканчике")


ice_cream = IceCreamStand(
    "Мороженко",
    "кафе-мороженое",
    4.8,
    ["ванильное", "шоколадное", "клубничное"],
    "Невский проспект, 20",
    "10:00 - 22:00"
)

print("Локация:", ice_cream.location)
print("Время работы:", ice_cream.working_hours)

ice_cream.show_flavors()

ice_cream.add_flavor("фисташковое")
ice_cream.remove_flavor("клубничное")

ice_cream.check_flavor("фисташковое")
ice_cream.check_flavor("клубничное")

ice_cream.ice_cream_on_stick()
ice_cream.soft_ice_cream()
ice_cream.ice_cream_in_cup()
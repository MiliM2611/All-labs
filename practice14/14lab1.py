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
    def __init__(self, restaurant_name, cuisine_type, rating, flavors):
        super().__init__(restaurant_name, cuisine_type, rating)
        self.flavors = flavors

    def show_flavors(self):
        print("Сорта мороженого:")
        for flavor in self.flavors:
            print(flavor)


ice_cream = IceCreamStand(
    "Мороженко",
    "кафе-мороженое",
    4.8,
    ["ванильное", "шоколадное", "клубничное", "фисташковое"]
)

ice_cream.show_flavors()
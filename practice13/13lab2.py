class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)


restaurant1 = Restaurant("ДедХо", "азиатская кухня")
restaurant2 = Restaurant("Вкусно и точка", "быстрое питание")
restaurant3 = Restaurant("Пхали Хинкали", "грузинская кухня")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
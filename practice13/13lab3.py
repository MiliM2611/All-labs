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


newRestaurant = Restaurant("ДедХо", "азиатская кухня", 4.5)

newRestaurant.describe_restaurant()

newRestaurant.update_rating(5)

newRestaurant.describe_restaurant()
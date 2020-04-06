class Restaurant():
	def __init__(self, restaurant_name, restaurant_type):
		self.name = restaurant_name
		self.type = restaurant_type
	def describe_restaurant(self):
		print("The restaurant's name is " + self.name.title() + ".")
		print("The restaurant's type is " + self.type + ".")
	def open_restaurant(self):
		print(self.name.title() + " is open.")
restaurant = Restaurant("haidilao", "hotpot")
restaurant.describe_restaurant()
restaurant.open_restaurant()
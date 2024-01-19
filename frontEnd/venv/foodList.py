from API import API
from FoodItem import FoodItem

class foodList:
    api = API()
    food_list = []
    food_dict = []

    def __init__(self, food_name):
        food_items = self.api.call_api(food_name)
        self.food_dict = self.api.call_api(food_name)
        for i in food_items:
            name = i.pop('item_name')
            brand = i.pop('brand_name')
            calories = i.pop('nf_calories')
            nutrient_dictionary = i
            food = FoodItem(name, brand, calories, nutrient_dictionary)
            self.food_list.append(food)

    def return_chosen(self, index):
        return self.food_dict[index]

    def return_list(self):
        return self.food_list

    def return_dict(self):
        return self.food_dict

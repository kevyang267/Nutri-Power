"""
This is a meal class. It contains a list of food items.

November 19, 2021 
- Created class
"""
NAME = 'item_name'
BRAND = 'brand_name'
CALORIES = 'nf_calories'
from FoodItem import FoodItem
from foodList import foodList

class meal:
    # Constructor for the class
    def __init__(self, name):
        # List of food items
        self.list_of_foods = []
        self.name = name
        self.calories = 0
        self.nutrition_dictionary = {}

    # Adding food to the list. Returns -1 
    # if the item is in the list and 0 if it added 
    # and item successfully.
    def add_foods(self, food_item):

        name = food_item.get_name()
        brand = food_item.get_brand()
        calories = food_item.get_calories()

        self.calories = self.calories + float(calories)

        if len(self.nutrition_dictionary) == 0:
            self.nutrition_dictionary = food_item.get_dictionary()
        else:
            for i in food_item.get_dictionary():
                if (i != 'nf_serving_size_unit') and (i != 'nf_serving_size_qty'):
                    if food_item.get_dictionary()[i] != 'null':
                        self.nutrition_dictionary[i] = float(self.nutrition_dictionary[i]) + float(food_item.get_dictionary()[i])

        self.list_of_foods.append(food_item)

    def get_name(self):
        return self.name
    
    def get_food_list (self):
        return self.list_of_foods

    # Returning a food item of the given name.
    # Returns a food item if found or None if none found.
    def find_food_item (self, food_name):
        
        # Loop through the list and find the item. 
        for i in self.list_of_foods:
            if i.get_name() == food_name:
                return i

        return None# No item found

    def total_cal(self):
        return self.calories

    def return_nutrient_profile(self):
        return self.nutrition_dictionary

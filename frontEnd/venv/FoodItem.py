"""
FoodItem class that is used to contain all of the information that a search food includes.

November 19, 2021
- Creation of class.


"""

from API import API

# Class definition 
class FoodItem:
    api = API()

    # Constructor for the class.

    def __init__(self, food_name, food_brand, food_calories, food_dict):
        self.__name = food_name
        self.__brand = food_brand
        self.__calories = food_calories
        self.__dictionary = food_dict

    def get_name (self):
        return self.__name

    def get_brand (self):
        return self.__brand
    
    def get_calories (self):
        return self.__calories
    
    def get_dictionary (self):
        return self.__dictionary

    # Might not need this one 
    def change_name(self, new_name):
        self.__name = new_name
     
    def change_calories(self, new_calorie):
        self.__calories = new_calorie

    # Method to add items to the dictionary. It returns -1 if there is an error 
    # or it returns 0 if it is able to add an item.


        









from flask import Flask, render_template, request, url_for, redirect
from person import person
from API import API
from FoodItem import FoodItem
from foodList import foodList
from meal import meal

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
# CORS(app)

userInfo = []
currentFoods = []
nutritionInfo = {}
foodItemList = []
personInfo = {}
user = person("male", 1, 1, 1, "light")
mealList = []
itemList = []
newDict = {}
calorieCount = 0


@app.route("/")
def home():
    return render_template('index.html',
                           data=[{'name': 'little'}, {'name': 'light'}, {'name': 'moderate'}, {'name': 'hard'}, {'name': 'work'}, {'name': 'athlete'}])


@app.route('/toList', methods=['GET', 'POST'])
def getList():
    if request.method == 'GET':
        print("Should never GET")

    if request.method == 'POST':
        form_data = request.form
        global currentFoods
        for key, value in form_data.items():
            foodItem = form_data.get('foodItem')
            currentFoods.append(foodItem)

        # foodItem = foodItemList[0]
        for i in foodItemList:

            brandName = i.get_brand()
            itemName = i.get_name()
            listItem = itemName + ", brand: " + brandName
            # print(listItem)
            print("Food item: ", foodItem)
            if (listItem == foodItem):
                foodItem = i
                break

        user.return_meal_at(0).add_foods(foodItem)
        # print(user.calculate_daily_nutrient_profile())

        global nutritionInfo
        nutritionInfo = user.calculate_daily_nutrient_profile()
        global calorieCount
        calorieCount = user.calculate_total_cal()

        print(calorieCount)

        keys = nutritionInfo.keys()

        global newDict

        for key in nutritionInfo:
            oldKey = key
            newKey = key
            newKey = newKey.replace("nf_", "")
            newKey = newKey.replace("_", " ")
            # print(key, nutritionInfo[key])
            newDict[newKey] = nutritionInfo[key]

        print(newDict)
        return render_template('index.html', nutrition_data=newDict, calories=calorieCount, selected_items=currentFoods, person_data=userInfo, scrollToAnchor='end')


@app.route('/foodData', methods=['GET', 'POST'])
def foodData():
    if request.method == 'GET':
        print("Should never GET")
    if request.method == 'POST':
        foods = []
        foodNames = []
        foodNames.clear()
        foods.clear()

        form_data = request.form
        count = 0
        global currentFoods
        global nutritionInfo
        global foodItemList
        for key, value in form_data.items():
            if (count == 0):
                print(value)
                food_list = foodList(value)
                foods = food_list.return_list()
                for i in foods:
                    brandName = i.get_brand()
                    itemName = i.get_name()
                    foodName = itemName + ", brand: " + brandName
                    foodNames.append(foodName)
                    foodItemList.append(i)

                # print("filler")

                # return_dictionary ["Food"] = value
            count = count + 1

            # print(form_data)
            print("List of foods: ", foods)
            print("Foods", foodNames)

        return render_template('index.html', nutrition_data=nutritionInfo,
                               calories=calorieCount, form_data=foodNames, selected_items=currentFoods, person_data=userInfo, scrollToAnchor='end')


@app.route('/data/', methods=['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':

        form_data = request.form

        # We will create a list.
        return_dictionary = []

        # Temporary values for the given attributes.
        counter = 0
        sex = "male"
        height = 1
        weight = 1
        age = 1
        exercise_level = "NO"

        # This will be for if the user wishes to bulk, maintain, or lose weight
        condition = "losing"

        # Creating values for the user.
        for key, value in form_data.items():

            if counter == 0:
                print(value)
                age = int(value)
                return_dictionary.append("Age: " + str(age))

            elif counter == 1:
                print(request.form['gender'])
                sex = value
                return_dictionary.append("Sex: " + sex)

            elif counter == 2:
                height = int(value)
                return_dictionary.append("Height: " + str(height))

            elif counter == 3:
                weight = int(value)
                return_dictionary.append("Weight: " + str(weight))

            elif counter == 4:
                exercise = request.form.get('exercise')
                exercise_level = exercise
                return_dictionary.append("Exercise: " + exercise_level)

            elif counter == 5:
                condition = value
                return_dictionary.append("Condition: " + condition)
            counter = counter + 1

        print("number of items: ", counter)
        # Create a temporary person with the given attributes

        # Kohei = person(sex, height, weight, age, exercise_level)
        global user

        user.change_age(age)
        user.change_weight(weight)
        user.change_exercise_level(exercise)
        user.change_height(height)
        user.change_sex(sex)

        # Add the final condition that the user has selected.
        if (condition.lower() == "maintain"):
            return_dictionary["Condition"] = user.return_maintenance()
        elif (condition.lower() == "bulk"):
            return_dictionary["Condition"] = user.return_bulking()
        elif (condition.lower() == "losing"):
            return_dictionary.append(
                "Maintenence Calorie Count: " + str(user.return_losing("moderate")))

        global userInfo
        userInfo = return_dictionary
        Kohei = return_dictionary

        # Returns a dictionary
        return render_template('index.html', person_data=return_dictionary, scrollToAnchor='end')


@app.route('/Login', methods=['GET', 'POST'])
def Login():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index'))

    # show the form, it wasn't submitted
    return render_template('login.html')


app.run(host='localhost', port=5000)

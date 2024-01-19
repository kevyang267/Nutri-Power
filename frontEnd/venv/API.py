"""
API Class to call the Nutrionix API
"""

class API:

    def __init__(self):
        import http.client
        self.conn = http.client.HTTPSConnection("nutritionix-api.p.rapidapi.com")

        self.headers = {
            'x-rapidapi-host': "nutritionix-api.p.rapidapi.com",
            'x-rapidapi-key': "83a686583amsh4b5dd474b143968p1989f2jsnf3a850b88cd6"
        }

    def call_api(self, item_name):
        split_name = item_name.split(' ')
        item_string = ''
        start = True
        for i in split_name:
            if start:
                item_string = i
                start = False
            else:
                item_string = item_string + "%20" + i

        item_string = "/v1_1/search/" + item_string + "=?fields=item_name%2Cbrand_name%2Cnf_calories%2Cnf_total_fat%2Cnf_saturated_fat%2Cnf_total_fat%2Cnf_trans_fatty_acid%2Cnf_total_carbohydrate%2Cnf_dietary_fiber%2Cnf_sugars%2Cnf_protein%2Cnf_cholesterol%2C%nf_calcium_dv%2Cnf_iron_dv%2Cnf_vitamin_a_dv%2Cnf_vitamin_c_dv%2Cnf_potassium"
        self.conn.request("GET", item_string, headers=self.headers)
        res = self.conn.getresponse()
        data = res.read()
        try:
            data_list = data.decode("utf-8").split("{")
            if data_list[1] == '"total_hits":0,"max_score":null,"hits":[]}':
                raise NameError
        except NameError:
            return "Invalid"
        index = 3;

        list_of_output = []
        while index != len(data_list) - 1:
            list_of_output.append(self.process_line(data_list[index]))
            index += 2

        return list_of_output

    def process_line(self, data_line):
        nutrient_dictionary = {}
        name = data_line[0:data_line.find("brand") - 2].replace('"', '')
        rest = data_line[data_line.find("brand") - 1:len(data_line) - 1].replace('}', '').replace('"', '')

        name_list = name.split(':')
        nutrient_dictionary[name_list[0]] = name_list[1]

        index = 0
        info_list = rest.split(',')
        while index != len(info_list):
            nutrient_info = info_list[index].split(':')
            nutrient_dictionary[nutrient_info[0]] = nutrient_info[1]
            index += 1

        return nutrient_dictionary

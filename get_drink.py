import requests
import random

class Drink():

    def __init__(self):
    # BASE ENDPOINT
        self.endpoint = "https://www.thecocktaildb.com/api/json/v1/1/"

    def get_random(self):
        # RETURN RANDOM COCKTAIL
        self.url = f"{self.endpoint}random.php"
        self.response = requests.get(self.url)
        self.data = self.response.json( )
        self.drinks = self.data["drinks"]

        # SELECT RANDOM DRINK FROM SEARCH RESULTS
        self.choice = random.choice(self.drinks)
        self.id = self.choice["idDrink"]
        # print(choice)
        # print(id)

        # SEARCH RANDOM SELECTION BY ID
        self.drink_url = f"https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i={self.id}"
        self.drink_response = requests.get(self.drink_url)
        self.drink_json = self.drink_response.json( )
        self.drink_data = self.drink_json["drinks"][0]
        # print(drink_data)

        # FORMAT RECIPE
        self.drink_name = self.drink_data["strDrink"]
        self.drink_ingredients = {self.drink_data["strMeasure1"]: self.drink_data["strIngredient1"],
                                  self.drink_data["strMeasure2"]: self.drink_data["strIngredient2"],
                                  self.drink_data["strMeasure3"]: self.drink_data["strIngredient3"],
                                  self.drink_data["strMeasure4"]: self.drink_data["strIngredient4"],
                                  self.drink_data["strMeasure5"]: self.drink_data["strIngredient5"],
                                  self.drink_data["strMeasure6"]: self.drink_data["strIngredient6"],
                                  self.drink_data["strMeasure7"]: self.drink_data["strIngredient7"],
                                  self.drink_data["strMeasure8"]: self.drink_data["strIngredient8"],
                                  self.drink_data["strMeasure9"]: self.drink_data["strIngredient9"],
                                  self.drink_data["strMeasure10"]: self.drink_data["strIngredient10"],
                                  self.drink_data["strMeasure11"]: self.drink_data["strIngredient11"],
                                  self.drink_data["strMeasure12"]: self.drink_data["strIngredient12"],
                                  self.drink_data["strMeasure13"]: self.drink_data["strIngredient13"],
                                  self.drink_data["strMeasure14"]: self.drink_data["strIngredient14"],
                                  self.drink_data["strMeasure15"]: self.drink_data["strIngredient15"]
                                  }
        self.drink_instructions = self.drink_data["strInstructions"]

        self.drink = [self.drink_name, self.drink_ingredients, self.drink_instructions]

        return self.drink


    def get_by_spirit(self, spirit):
        # SEARCH BY LIQUOR
        self.spirit = spirit
        self.url = f"{self.endpoint}filter.php?i={self.spirit}"
        self.response = requests.get(self.url)
        self.data = self.response.json()
        self.drinks = self.data["drinks"]

        # SELECT RANDOM DRINK FROM SEARCH RESULTS
        self.choice = random.choice(self.drinks)
        self.id = self.choice["idDrink"]
        # print(choice)
        # print(id)

        # SEARCH RANDOM SELECTION BY ID
        self.drink_url = f"https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i={self.id}"
        self.drink_response = requests.get(self.drink_url)
        self.drink_json = self.drink_response.json()
        self.drink_data = self.drink_json["drinks"][0]
        # print(drink_data)

        # FORMAT RECIPE
        self.drink_name = self.drink_data["strDrink"]
        self.drink_ingredients = {self.drink_data["strMeasure1"]:self.drink_data["strIngredient1"],
        self.drink_data["strMeasure2"]:self.drink_data["strIngredient2"],
        self.drink_data["strMeasure3"]:self.drink_data["strIngredient3"],
        self.drink_data["strMeasure4"]:self.drink_data["strIngredient4"],
        self.drink_data["strMeasure5"]:self.drink_data["strIngredient5"],
        self.drink_data["strMeasure6"]:self.drink_data["strIngredient6"],
        self.drink_data["strMeasure7"]:self.drink_data["strIngredient7"],
        self.drink_data["strMeasure8"]:self.drink_data["strIngredient8"],
        self.drink_data["strMeasure9"]:self.drink_data["strIngredient9"],
        self.drink_data["strMeasure10"]:self.drink_data["strIngredient10"],
        self.drink_data["strMeasure11"]:self.drink_data["strIngredient11"],
        self.drink_data["strMeasure12"]:self.drink_data["strIngredient12"],
        self.drink_data["strMeasure13"]:self.drink_data["strIngredient13"],
        self.drink_data["strMeasure14"]:self.drink_data["strIngredient14"],
        self.drink_data["strMeasure15"]:self.drink_data["strIngredient15"]
            }
        self.drink_instructions = self.drink_data["strInstructions"]

        self.drink = [self.drink_name, self.drink_ingredients, self.drink_instructions]

        return self.drink

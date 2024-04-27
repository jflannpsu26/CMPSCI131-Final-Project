class FoodItem:

    # Define constructor with parameters to initialize instance
    def __init__(self, name="", fat=0, carbs=0, protein=0):
        self.name = name
        self.fat = fat 
        self.carbs = carbs 
        self.protein = protein 

    def get_calories(self, num_servings): #function to calculate calories
        # Calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings
        return calories 

    def print_info(self): #prints out nutritional information
        header ="Nutritional Information:"
        centeredHeader = header.center(96) #centers the header
        print(centeredHeader)
        print(f'{"Number of grams of fat: ":64} {self.fat:.2f} {"for a serving"}')
        print(f'{"Number of grams of carbs: ":64}{self.carbs:.2f} {"for a serving"}')
        print(f'{"Number of grams of protein: ":64} {self.protein:.2f} {"for a serving"}')

if __name__ == "__main__":    

    item_name = input("Name of food or liquid: ")

    if item_name == 'water' or item_name=="Water": #if food or liquid is water, it returns the following lines
        food_item = FoodItem()
        food_item.print_info()
        print(f'{"Number of calories for 1.0 serving(s): ":64} {food_item.get_calories(1.0):.2f}' ' Calores')                       

    else:
        amount_fat = float(input("Grams of Fat: ")) #asks for the amount of other stuff that a food label woud display
        amount_carbs = float(input("Grams of Carbs: "))
        amount_protein = float(input("Grams of Protein: "))
        num_servings = float(input("Number of Servings: "))       

        food_item = FoodItem(item_name, amount_fat, amount_carbs, amount_protein) #calculates the caloties
        food_item.print_info() #prints out the information that the user just inserted
        print(f'{"Number of calories for 1.0 serving(s): ":64} {food_item.get_calories(1.0):.2f}' ' Calories')
        print(f'{"Number of calories for"} {num_servings:.2f} {"serving(s): ":36} {food_item.get_calories(num_servings):.2f}' ' Calories')
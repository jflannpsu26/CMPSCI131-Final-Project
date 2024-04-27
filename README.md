This final project covered all of the concepts that were covered throughout the introductory Python course that I was enrolled in at Penn State Schuylkill in the Spring of 2024.  I was assigned 5 programs throughout the course of a week that I had to complete. I will provide the description and objectives of the programs here:

**1. Nutritional Information Classes Chapter 9 (15 points)**

 

Please create a program using only python syntax to resolve the scenario below:

The scenario will provide the suggested and/or exact syntax to be used. 

Scenario:

Provided the following partial python program:

Complete the FoodItem class by adding a constructor to initialize a food item. The constructor

should initialize the name (a string) to "Water" and all other instance attributes to 0.0 by default. If

the constructor is called with a food name, grams of fat, grams of carbohydrates, and grams of

protein, the constructor should assign each instance attribute with the appropriate parameter

value.

The given program accepts as input a food item name, amount of fat, carbs, and protein, and the

number of servings. The program creates a food item using the constructor parameters' default

values and a food item using the input values. The program outputs in table format the nutritional

information and calories per serving for a food item.

 

input values: 

Water
M&M’s 10 grams of fat, 34 grams of carbs, and 2 grams of protein, and 3 servings
 

class FoodItem:

    # TODO: Define constructor with parameters to initialize instance

    #    ADD   attributes (name, fat, carbs, protein)

    def get_calories(self, num_servings):

        # Calorie formula

        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings;

        return calories 

    def print_info(self):

        # Print nutritional information per serving include fat, carbs, and protein to 2 decimals

if __name__ == "__main__":    

    item_name = input()

    if item_name == 'Water' or item_name == 'water':

        food_item = FoodItem()

        food_item.print_info()

        print(f'Number of calories for {1.0:.2f} serving(s): {food_item.get_calories(1.0):.2f}')                       

    else:

        amount_fat = float(input())

        amount_carbs = float(input())

        amount_protein = float(input())

        num_servings = float(input())       

        food_item = FoodItem(item_name, amount_fat, amount_carbs, amount_protein)

        food_item.print_info()

        print(f'Number of calories for {1.0:.2f} serving(s): {food_item.get_calories(1.0):.2f}')

        print(f'Number of calories for {num_servings:.2f} serving(s): {food_item.get_calories(num_servings):.2f}')


**2: String and index slicing**

Please create a program using only python syntax to resolve the scenario below:

The scenario will provide the suggested and/or exact syntax to be used. 

Scenario:

Use the following paragraph as your original database:

Nearly ten years had passed since the Dursleys had woken up to find their nephew on the front step, but Privet Drive had hardly changed at all. The sun rose on the same tidy front gardens and lit up the brass number four on the Dursleys' front door; it crept into their living room, which was almost exactly the same as it had been on the night when Mr. Dursley had seen that fateful news report about the owls. Only the photographs on the mantelpiece really showed how much time had passed. Ten years ago, there had been lots of pictures of what looked like a large pink beach ball wearing different-colored bonnets - but Dudley Dursley was no longer a baby, and now the photographs showed a large blond boy riding his first bicycle, on a carousel at the fair, playing a computer game with his father, being hugged and kissed by his mother. The room held no sign at all that another boy lived in the house, too.  Yet Harry Potter was still there, asleep at the moment, but not for long. His Aunt Petunia was awake and it was her shrill voice that made the first noise of the day.

Using the concepts from Chapter 7 (string slicing), generate the following sentences from the paragraph above.   The original database must be a py file you access to obtain the words to generate (print out) the following phrase:

Harry put the photo of Dudley on the mantel.  There is no sign of aunt Petunia’s baby bonnet in the house


**3: Age Seniority** 


Please create a program using only python syntax to resolve the scenario below:

The scenario will provide the suggested and/or exact syntax to be used. 

Scenario:

Calculate the person’s age based on their birth date. If the person’s age is within 3 months of a given date (which will be provided), you will need to print out the names and age.  You will be provided three ages and specific dates below:

 

With the txt file provided create a dictionary containing the person’s first name, last name, and birthdate.
Calculate each person’s age (years/months) in the database and import into an age_dictionary. I will be printing this database when I grade the program to verify accuracy of age.  You do not have to have a print statement for the age_dictionary in the python program.
“Key” the age in the age_dictionary to loop through the dictionary to identify and print the person who age is with three months of the following dates:
First test of the program will be:   anyone in the database 62 by July 1, 2024
Second test of the program will be: anyone in the database 65 by January 1, 2025
Third test of the program will be : anyone in the database 67 by March 1, 2025
Remember you will need an input statement for each “test” of the age and dates requested.
Print out will be the list of individuals that meet the “test” criteria.
I will run the program three times with the “test” criteria in addition to the age_dictionary contents.
 




**4: Area Code Exchange**

Scenario:

The area code for Smallville, USA has change from 413 to 863.  You will need to update and append the provided database.  You will need to create a dictionary/list containing first_name, last_name, area code and phone number.   You will need to append/update the database for any future entries into the database that contain the incorrect area code.

With the txt file provided create a dictionary containing the person’s first, last, area code, and phone number.
“Key” the area code so that you can update/append the data base. Create a new dictionary with the new phone numbers.
You will need an input statement for new names and phone numbers to the database.
The program must include a “check” of the old area code and replace with the new area code.
Print out the 863_database.
My test of the program will be to print 413_database and then print the 863-database. I will then add data to the 413_database and verifies it converts and prints out the updated 863_database.



5: Payroll System:


Scenario:

                  At the beginning of the semester, we worked on a mini program to calculate a person’s two-week gross wage.  Using the concept from the original program, we will create a payroll system (python program) to generate a paystub (print out in table format) for your company employees.

Information:   

Employee works 40 hours per week.
Over time is considered anything over 80 hours in two weeks. Program must have a defined function for overtime.
Employee: Joe Burns – works 82 hours in two weeks.  Current hourly wage is $28.50
Employee: Sam Nelson – works 86 hours in two weeks.  Current hourly wage is $29.25
Employee: Tim Matters – works 75 hours in two weeks.  Current hourly wage is $19.75
Calculate 20% for taxes to calculate the “net pay”
Program must have an input statement that asks, “Enter hours worked for xxxx”. Where xxxx is the employee’s name. You may need to use a list or dictionary to store the employee’s name and wage information.
Remember the employee does not work the same number of hours every week.
Program must have a formatted output statement with defined columns (easily readable).
Print out should look like a pay stub with name, total hours, wage, gross pay, taxes, and net pay. (Use table formatting from Chapter 7)



database = { #database that was taken from text file and placed into ageDatabase Python file
"Sandy Chair": "12/06/1941", #names and birthdays are split so it is easier"
"Joan Table": "02/13/1968",
"Bob Couch": "04/09/1997",
"Gene Counter": "10/02/1964",
"Mark Martin": "12/22/1975",
"Steve Center": "03/25/1980",
"Albert Market": "06/03/1940",
"Sonya Spoon": "07/20/1996",
"Matt Door": "07/15/1934",
"Shawn Bottle": "09/27/1919",
"Joe Grass": "06/27/1922",
"Dennis Smith": "11/19/1969",
"Tara Lutz": "03/01/1911",
"Roxane Ruggles": "03/26/1964",
"Terry Beverage": "05/10/1982",
"Kerry Juice": "07/07/1971",
"Ryan Rodd ":  "11/20/2000",
"Zach Gunner": "05/20/1945",
"George Glass": "10/04/1934"}

def calculate_age(birthday, reference_date): #calculates a person's age
    birth_month, birth_day, birth_year = map(int, birthday.split('/')) #splits the string
    reference_month, reference_day, reference_year = map(int, reference_date.split('/')) #splits the string

    years = reference_year - birth_year
    months = reference_month - birth_month
    days = reference_day - birth_day

    if months < 0 or (months == 0 and days <0):
        years -=1

    if months < 0:
        months += 12
    if days < 0:
        reference_month -= 1
        if reference_month == 0:
            reference_month = 12
        days +=(30 - birth_day) + reference_day
    
    return years, months
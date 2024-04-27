from ageDatabase import database, calculate_age #imports varibales from ageDatabase

def main():
   
    # Input reference date
    reference_date = input("Enter the reference date (MM/DD/YYYY): ") #the reference date that the program will use

    # Input age threshold
    age_threshold = int(input("Enter the age threshold: ")) #this is the age that will filter out the list

    # See who falls into the new database
    print("People whose age is within 3 months of the reference date and meet the age threshold:")
    for person, birth_date in database.items():
        years, months = calculate_age(birth_date, reference_date)
        if years >= age_threshold and abs(months) <= 3: 
            print(f"{person} - {years} years {abs(months)} months") #prints out the person's age and months if they reach the age threshold by the reference date

if __name__ == "__main__":
    main()
import areaCodeDatabase #imports the areaCodeDatabase Python File
# took inspiration from dictionary 8.12 example, used the format from that program to do this program.


info_prompt = "Enter name, area code, and phone number: "
del_error = "No names in the system. Try this."
menu_prompt = ("1. Add Contact\n" #menu
                "2. Print 413 database\n"
                "3. Print 863 databases\n"
                "4. Quit\n") #exits the program

def print_database(database): #function that prints out the databases into a neat table 
    print("{:<15} {:<15} {:<10} {:<15}".format("First Name", "Last Name", "Area Code", "Phone Number"))
    for entry in database:
        print("{:<15} {:<15} {:<10} {:<15}".format(entry["first_name"], entry["last_name"], entry["area_code"], entry["phone_number"]))


while True:  # Exit when user enters no input
    command = input(menu_prompt).lower().strip() 
    if command == '1':
        firstName,lastName, areaCode, number = input(info_prompt).split() #allows the user to put in first name, last name, areacode, and phone number into one input line
        if areaCode == 413: #if area code is 413, change it to 863 due to zip code change
            areaCode = 863
        areaCodeDatabase.newDatabase.append({ #allows you to update the new database by taking the inputs from first name, last name, area code, and number.
            "first_name": firstName,
            "last_name": lastName,
            "area_code": str(areaCode),  # Convert back to string for consistency
            "phone_number": number
        })
    elif command == '2':
        print_database(areaCodeDatabase.oldDatabase) #prints out the old database and uses the print_database function to be more neat
        
    elif command == '3':
        print_database(areaCodeDatabase.newDatabase) #prints out the new database and uses the print_database function to make table more neat
    elif command == '4': #exits the program
        break
    else:
        print('Unrecognized command.') #this is for the menu, if the user puts anything else than numbers 1-4
    print()
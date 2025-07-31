import datetime
import write

def display_lands(lands):
    print("Listing all lands:")
    print("Kitta   |         Location      |      Anna    |              Price     |            Status ")
    print("================================================================================================")

    for kitta, land in lands.items():
        print("" + kitta + " \t|\t " + land['city'] + " \t|\t " + str(land['area']) + " \t|\t  NRP: " + str(land['price']) + " \t|\t " + land['status'])
        
def rent_land(lands):
    display_lands(lands)
    print("================================================================================================")
    customer = input("\nEnter your name: ").strip()
    phone_number = input("Enter your phone number (10 digits): ").strip()
    while not phone_number.isdigit() or len(phone_number) != 10:
        print("Invalid phone number. Please enter a 10-digit phone number.")
        phone_number = input("Enter your phone number (10 digits): ").strip()

    kitta = input("Enter the kitta number of the land you want to rent: ").strip()
    if kitta in lands and lands[kitta]['status'] == 'Available':
        anna = int(input("Enter the anna amount for the land (must take all available anna): ").strip())
        duration = int(input("Enter the rental duration in months: ").strip())
        if anna == lands[kitta]['area']:
            lands[kitta]['status'] = 'Rented'
            write.generate_invoice(kitta, duration, customer, lands, phone_number)
            more = input("Do you want to rent more land? (yes/no): ").strip().lower()
            while more == 'yes':
                display_lands(lands)
                kitta = input("Enter the kitta number of the land you want to rent: ").strip()
                if kitta in lands and lands[kitta]['status'] == 'Available':
                    anna = int(input("Enter the anna amount for the land (must take all available anna): ").strip())
                    duration = int(input("Enter the rental duration in months: ").strip())
                    if anna == lands[kitta]['area']:
                        lands[kitta]['status'] = 'Rented'
                        write.generate_invoice(kitta, duration, customer, lands, phone_number)
                    else:
                        print("You must rent all available anna for this land.")
                else:
                    print("Invalid kitta number or land is already rented.")
                more = input("Do you want to rent more land? (yes/no): ").strip().lower()
        else:
            print("You must rent all available anna for this land.")
    else:
        print("Invalid kitta number or land is already rented.")

def return_land(lands):
    kitta = input("Enter the kitta number of the land you want to return: ").strip()
    if kitta in lands and lands[kitta]['status'] == 'Rented':
        months = int(input("How many months did you rent the land?: ").strip())
        extra_months = int(input("How many extra months (if any) did you use the land?: ").strip())
        fines = extra_months * 0.10 # NPR 100 fine per extra month
        total_without_fine = months * lands[kitta]['price']
        total_due = total_without_fine + fines
        print("\n*************************************************************")
        print("Return Invoice")
        print("Land Kitta Number: " + kitta)
        print("Extra Months: " + str(extra_months))
        print("Fine for Late Return: NPR " + str(fines))
        print("Total Amount Without Fine: NPR " + str(total_without_fine))
        print("Total Amount Due: NPR " + str(total_due))
        print("*************************************************************")
        print("Thank you for choosing TechnoPropertyNepal!")
        lands[kitta]['status'] = 'Available'
    else:
        print("Invalid kitta number or land is already available.")


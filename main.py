import operation
import read

def main():
    lands = read.load_lands()
    while True:
        print("Press 1 to Rent Land")
        print("Press 2 to Return Land.")
        print("Press 3 to Exit from the system.")
        
        choice = input("Enter your choice (1-3): ").strip()

        if choice == '1':
            operation.rent_land(lands)
        elif choice == '2':
            operation.return_land(lands)
        elif choice == '3':
            read.save_lands(lands)
            print("Exiting... Thank you for using our service!")
            print("*" * 106)
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")
            print("*" * 106)

if __name__ == "__main__":
    main()

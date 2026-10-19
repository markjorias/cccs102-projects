## TASK GUIDE ##
#Enter instrument type: Guitar
#Enter rental price: 500
#Is the instrument available? (True/False): True
#Guitar rental created with price 500.00
#Do you want to rent or return the instrument? (Rent/Return): Rent
#A Guitar has been rented for 500.00


def main():
    instrument_type = input("Enter instrument type: ")
    while True:
        rental_price = input("Enter rental price: ")
        if rental_price.isdigit() == True:
            break
        else:
            print  ("Invalid input. Please enter a number only.")

    while True:
        available = input("Is the instrument available? (True/False): ").lower()
        if available.lower() == 'true':
            print(f"{instrument_type} rental created with price PHP{rental_price}.00")
            break
        elif available.lower() == 'false':
            print(f"{instrument_type} is not available")
            break
        else:
            print("Invalid input. Please enter 'True' or 'False'")

    while True:
        action = input("Do you want to rent or return the instrument? (Rent/Return): ")
        if action.lower() == 'rent':
            print(f"A {instrument_type} has been rented for ₱{rental_price}.00")
            break
        elif action.lower() == 'return':
            print(f"The {instrument_type} has been returned.")
            break
        else:
            print("Invalid action. Please choose 'Rent' or 'Return'")

if __name__ == "__main__":
    main()
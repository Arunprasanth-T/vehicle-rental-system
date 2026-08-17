from car import Car
from bike import Bike
from rental_system import RentalSystem


def main():

    rental_system = RentalSystem()

   
    car1 = Car("TN01AB1234", "Toyota", 1500, 5)
    car2 = Car("TN02CD5678", "Honda", 1200, 4)

   
    bike1 = Bike("TN03EF9012", "Yamaha", 700, "150 CC")
    bike2 = Bike("TN04GH3456", "Royal Enfield", 900, "350 CC")

    rental_system.add_vehicle(car1)
    rental_system.add_vehicle(car2)
    rental_system.add_vehicle(bike1)
    rental_system.add_vehicle(bike2)

    while True:

        print("\n" + "=" * 40)
        print("      VEHICLE RENTAL SYSTEM")
        print("=" * 40)
        print("1. Display Vehicles")
        print("2. Rent Vehicle")
        print("3. Return Vehicle")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":

            rental_system.display_vehicles()

        elif choice == "2":

            vehicle_number = input("Enter vehicle number: ")

            try:
                days = int(input("Enter rental days: "))
                rental_system.rent_vehicle(vehicle_number, days)
            except ValueError:
                print("Please enter a valid number of days.")

        elif choice == "3":

            vehicle_number = input("Enter vehicle number: ")
            rental_system.return_vehicle(vehicle_number)
        
        elif choice == "4":

            print("Thank you for using Vehicle Rental System.")
            break

        else:

            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
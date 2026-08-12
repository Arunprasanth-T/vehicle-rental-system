class RentalSystem:

    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def display_vehicles(self):
        print("\n========== VEHICLES ==========")

        for vehicle in self.vehicles:
            vehicle.display_details()
            print("-" * 40)

    def rent_vehicle(self, vehicle_number, days):

        if days <= 0:
            print("Rental days must be greater than 0.")
            return

        for vehicle in self.vehicles:

            if vehicle.vehicle_number == vehicle_number:

                if not vehicle.is_available:
                    print("Vehicle is already rented.")
                    return

                total_amount = vehicle.calculate_rental_amount(days)
                vehicle.is_available = False

                print("\n========== RENTAL DETAILS ==========")
                print("Vehicle Number :", vehicle.vehicle_number)
                print("Brand          :", vehicle.brand)
                print("Rental Days    :", days)
                print("Total Amount   : ₹", total_amount, sep="")
                print("Status         : Successful")

                return

        print("Vehicle not found.")
from vehicle import Vehicle


class Bike(Vehicle):

    def __init__(self, vehicle_number, brand, rental_price, engine_capacity):
        super().__init__(vehicle_number, brand, rental_price)
        self.engine_capacity = engine_capacity

    def display_details(self):
        print("Vehicle Type    : Bike")
        print("Vehicle Number  : ", self.vehicle_number)
        print("Brand           : ", self.brand)
        print("Engine Capacity : ", self.engine_capacity)
        print("Rental Price    : ₹", self.rental_price, "/day", sep="")
        print(
            "Available       : ",
            "Yes" if self.is_available else "No"
        )

    def calculate_rental_amount(self, days):
        return self.rental_price * days
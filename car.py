from vehicle import Vehicle


class Car(Vehicle):

    def __init__(self, vehicle_number, brand, rental_price, number_of_seats):
        super().__init__(vehicle_number, brand, rental_price)
        self.number_of_seats = number_of_seats

    def display_details(self):
        print("Vehicle Type   : Car")
        print("Vehicle Number : ", self.vehicle_number)
        print("Brand          : ", self.brand)
        print("Seats          : ", self.number_of_seats)
        print("Rental Price   : ₹", self.rental_price, "/day", sep="")
        print(
            "Available      : ",
            "Yes" if self.is_available else "No"
        )

    def calculate_rental_amount(self, days):
        return self.rental_price * days
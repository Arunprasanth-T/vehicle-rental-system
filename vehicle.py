from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, vehicle_number, brand, rental_price):
        self.vehicle_number = vehicle_number
        self.brand = brand
        self.rental_price = rental_price
        self.is_available = True

    @abstractmethod
    def display_details(self):
        pass

    @abstractmethod
    def calculate_rental_amount(self, days):
        pass
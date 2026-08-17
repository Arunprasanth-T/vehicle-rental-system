# Vehicle Rental System

A simple Vehicle Rental System developed using Python and Object-Oriented Programming (OOP).

The system supports different types of vehicles such as Cars and Bikes. Users can view vehicle details, rent a vehicle, and calculate the rental amount based on the number of rental days.

## Features

- Create different types of vehicles
- Store common vehicle information
- Store vehicle-specific information
- Display vehicle details
- Calculate rental amount
- Track vehicle availability
- Prevent renting an already rented vehicle
- Handle invalid input
- Demonstrate multiple types of vehicles

## OOP Concepts Used

### Abstraction

`Vehicle` is an abstract base class that defines common methods for all vehicles.

### Inheritance

`Car` and `Bike` inherit from the `Vehicle` class.

### Encapsulation

Vehicle-related data is maintained inside the respective classes.

### Polymorphism

`Car` and `Bike` provide their own implementations of:

```python
display_details()
calculate_rental_amount()
## Return Vehicle

The system allows users to return a rented vehicle.

When a vehicle is successfully rented, its availability status is changed to `False`. When the vehicle is returned, the status is changed back to `True`.

### Return Process

```text
Available
    ↓
  Rent
    ↓
Rented
    ↓
 Return
    ↓
Available
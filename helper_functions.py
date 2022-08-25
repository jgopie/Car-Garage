from customer_class import Customer
from vehicle_class import Vehicle


def add_new_customer():
    new_customer = Customer()
    new_customer.set_name(input("Enter customer name: "))
    return new_customer


def add_new_vehicle():
    new_vehicle = Vehicle()
    new_vehicle.set_make(input("Enter vehicle make: "))
    new_vehicle.set_model(input("Enter vehicle model: "))
    new_vehicle.set_year(input("Enter vehicle year: "))
    new_vehicle.set_license_plate(input("Enter vehicle license plate: "))
    return new_vehicle

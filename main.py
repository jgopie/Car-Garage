from helper_functions import *

jordan = add_new_customer()
my_car = add_new_vehicle()
jordan.add_car(my_car)
print(jordan.get_cars())
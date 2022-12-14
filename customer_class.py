class Customer:

    def __init__(self, name="Default"):
        self._customer_name = name
        self._customer_cars = []
        self._customer_id = None

    def set_name(self, name):
        if isinstance(name, str):
            self._customer_name = name
        else:
            print("Invalid name provided.")
            return

    def get_name(self):
        return self._customer_name

    def get_id(self):
        return self._customer_id

    def add_car(self, vehicle):
        self._customer_cars.append(vehicle)

    def get_cars(self):
        return self._customer_cars

    def __repr__(self):
        return f"Name: {self._customer_name}\nID: {self._customer_id}"

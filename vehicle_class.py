class Vehicle:
    def __init__(self):
        self._license_plate = 0
        self._make = None
        self._model = None
        self._owner = None
        self._year = None

    def set_license_plate(self, plate):
        self._license_plate = plate

    def get_license_plate(self):
        return self._license_plate

    def set_make(self, make):
        self._make = make

    def get_make(self):
        return self._make

    def set_owner(self, owner):
        self._owner = owner

    def set_model(self, model):
        self._model = model

    def get_model(self):
        return self._model

    def get_owner(self):
        return self._owner

    def set_year(self, year):
        self._year = year

    def get_year(self):
        return self._year

    def __repr__(self):
        return f"\nMake: {self._make}\nModel: {self._model}\nYear: {self._year}\nOwner: {self._owner}\nLicense Plate: {self._license_plate} "

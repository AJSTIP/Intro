class Information:
    def __init__(self, name, age, address, phone):
        self._name = name
        self._age = age
        self._address = address
        self._phone = phone

    # Getters
    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def get_address(self):
        return self._address

    def get_phone(self):
        return self._phone

    # Setters
    def set_name(self, name):
        self._name = name

    def set_age(self, age):
        self._age = age

    def set_address(self, address):
        self._address = address

    def set_phone(self, phone):
        self._phone = phone

    def display(self):
        print(f"Name: {self._name}, Age: {self._age}, Address: {self._address}, Phone: {self._phone}")
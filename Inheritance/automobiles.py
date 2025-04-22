class Automobiles:
    def __init__(self, make, model, year, mileage, price):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.price = price

    # Getter methods
    def get_make(self):
        return self.make

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_mileage(self):
        return self.mileage

    def get_price(self):
        return self.price

    def get_info(self):
        return f"{self.year} {self.make} {self.model} with mileage: {self.mileage} miles and price: ${self.price}"

class Car(Automobiles):
    def __init__(self, make, model, year, mileage, price, doors):
        super().__init__(make, model, year, mileage, price)
        self.doors = doors

    def get_info(self):
        return f"{super().get_info()} with {self.doors} doors"

class Truck(Automobiles):
    def __init__(self, make, model, year, mileage, price, payload_capacity):
        super().__init__(make, model, year, mileage, price)
        self.payload_capacity = payload_capacity

    def get_info(self):
        return f"{super().get_info()} with a payload capacity of {self.payload_capacity} tons"

class SUV(Automobiles):
    def __init__(self, make, model, year, mileage, price, off_road_capability):
        super().__init__(make, model, year, mileage, price)
        self.off_road_capability = off_road_capability

    def get_info(self):
        return f"{super().get_info()} with off-road capability: {self.off_road_capability}"

def main():
    vehicles = [
        Car("Toyota", "Camry", 2020, 50000, 23566, 4),
        Truck("Ford", "F-150", 2019, 2000, 60000, 2),
        SUV("Jeep", "Wrangler", 2021, 50, 62000, True),
        Automobiles("Generic", "Vehicle", 2022, 10000, 30000)
    ]

    for vehicle in vehicles:
        print(vehicle.get_info())

if __name__ == "__main__":
    main()
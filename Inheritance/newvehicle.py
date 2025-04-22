import automobiles as auto

def main():
    car1 = auto.Car("Toyota", "Camry", 2020, 50000, 23566, 4)
    truck1 = auto.Truck("Ford", "F-150", 2019, 2000, 60000, 2)
    suv1 = auto.SUV("Jeep", "Wrangler", 2021, 50, 62000, True)

    print(f"Car Make: {car1.get_make()}, Model: {car1.get_model()}, Year: {car1.get_year()}, Mileage: {car1.get_mileage()}, Price: {car1.get_price()}, Doors: {car1.doors}")
    print(f"Truck Make: {truck1.get_make()}, Model: {truck1.get_model()}, Year: {truck1.get_year()}, Mileage: {truck1.get_mileage()}, Price: {truck1.get_price()}, Payload Capacity: {truck1.payload_capacity} tons")
    print(f"SUV Make: {suv1.get_make()}, Model: {suv1.get_model()}, Year: {suv1.get_year()}, Mileage: {suv1.get_mileage()}, Price: {suv1.get_price()}, Off-road Capability: {suv1.off_road_capability}")

if __name__ == "__main__":
    main()
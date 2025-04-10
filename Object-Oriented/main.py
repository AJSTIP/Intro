class Person:
    def __init__(self, name, age, location): 
        self.name, self.age, self.location = name, age, location

    def __str__(self): 
        return f"Hello, my name is {self.name} and I am {self.age} years old. {self.location}"

class Location:
    def __init__(self, city, country): 
        self.city, self.country = city, country

    def __str__(self): 
        return f"I live in {self.city}, {self.country}."

if __name__ == "__main__":
    print(Person("Alice", 30, Location("New York", "USA")))
    print(Person(input("Enter name: "), int(input("Enter age: ")), Location(input("Enter city: "), input("Enter country: "))))


# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I make a sound."

# Derived class 1
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# Derived class 2
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Derived class 3
class Bird(Animal):
    def speak(self):
        return f"{self.name} says Chirp!"

# Main function to demonstrate inheritance
def main():
    animals = [
        Dog("Buddy"),
        Cat("Whiskers"),
        Bird("Tweety"),
        Animal("Generic Animal")
    ]

    for animal in animals:
        print(animal.speak())

if __name__ == "__main__":
    main()
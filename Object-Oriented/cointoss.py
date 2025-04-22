#   The class constructor works as a blueprint for the object, 
#   We can create as many objects as we want using the same blueprint 
#   and each object will have its own copy of the attributes defined in the constructor.
#   The constructor is defined using the __init__ method.
#   Using self helps to differentiate between the attributes of the class and the attributes of the object.  

class Coin:
    def __init__(self):
        self.sideup = 'Heads' # Default value for the coin side
        # The constructor initializes the coin to 'Heads' when a new Coin object is created.
    
    def toss(self):
        import random
        self.sideup = 'Heads' if random.randint(0, 1) == 0 else 'Tails'

    def get_sideup(self):
        return self.sideup # This method returns the current side of the coin.

    def __str__(self):
        return f"Coin is showing: {self.sideup}" # This method returns a string representation of the Coin object, which is useful for printing the object directly.

# Code below in the main function is an example of how to use the Coin class.
# It creates three Coin objects and tosses 2 of them multiple times, then printing the results.

def main():
    my_coin = Coin()
    my_coin2 = Coin()
    my_coin3 = Coin()

    for i in range(10):  # Run the program 10 times
        coin(i, my_coin, my_coin2)
        
    print("Final state of Coin3:", my_coin3)  # Accessing the state of Coin3 using __str__
    print(f"Final state of Coin1 & Coin 2: {my_coin} and {my_coin2}")  # Accessing the state of Coin1 and Coin2 using __str__


def coin(i, my_coin, my_coin2):
    print(f"Run {i + 1}:")
    print("Initial state of Coin1:", my_coin)
    print("Initial state of Coin2:", my_coin2)
    

    # Toss first two coins
    my_coin.toss()
    my_coin2.toss()

    print("After toss, state of Coin1:", my_coin)
    print("After toss, state of Coin2:", my_coin2)
    print('-' * 40)  # Add a dashed line for readability

if __name__ == "__main__":
    main()
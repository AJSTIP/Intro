import cointoss

def toss(obj): # This function takes a Coin object as an argument and tosses it.
    print("Tossing the coin...")
    obj.toss()

def status(obj): # This function takes a Coin object as an argument and prints its current side.
    print("Checking the coin status...")
    print(f"The current side is {obj.get_sideup()}")
    
def process_coin(): # This function creates a Coin object, tosses it, and checks its status.
    print("Creating a new coin...")
    coin = cointoss.Coin()
    toss(coin)
    status(coin)

def main():
    for _ in range(2):
        process_coin()

if __name__ == "__main__":
    main()
    input("Press Enter to exit...")
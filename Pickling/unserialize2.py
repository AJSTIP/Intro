import pickle

def main():
    try:
        # Open the file in binary read mode
        in_file = open('emp.dat', 'rb')

        print("Reading data from the file...\n")

        # Read and display all objects in the file
        while True:
            try:
                person = pickle.load(in_file)
                print(f"Name: {person['name']}")
                print(f"Age: {person['age']}")
                print(f"Weight: {person['weight']} lbs")
                print("-" * 30)
            except EOFError:
                # End of file reached
                break

        in_file.close()

    except FileNotFoundError:
        print("The file 'emp.dat' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
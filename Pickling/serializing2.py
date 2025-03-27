import pickle

def main():
    out_file = open('emp.dat', 'wb')

    repeat = 'y'

    while repeat.lower() == 'y':  # Fixed the condition to call lower()
        write_data(out_file)

        repeat = input('Do you want to enter more information? (Y/N):   ')

    out_file.close()

# Create and dump objects into file
def write_data(file):
    person = {}

    person['name'] = input('Enter the name:   ')
    person['age'] = input('Enter the age:   ')
    person['weight'] = input('Enter the weight in (LBS):    ')

    print(person)

    pickle.dump(person, file)

if __name__ == '__main__':
    main()
try:
    #Add Main Dictionary
    phonebook = {
        "John": '123-456789',
        "Jane": '987-654321',
        "Doe": '456-789123',
    }

    # Add new entries for the phonebook
    phonebook['Kevin'] = '321-654987'
    del phonebook['Doe']
    # del phonebook['Peter'] - This will raise a KeyError if 'Peter' is not in the dictionary

    #PopItem removes the last item from the dictionary and returns it as a tuple
    #Pop removes the specified key and returns its value
    ph_num = phonebook.popitem()

    # Ask the user for a name and check if it exists in the phonebook,
    # if it does, print the number, otherwise add it with a default number
    # and print the contents of the phonebook
    u_input = input("Enter a name: ")
    if u_input in phonebook:
        print(f"{u_input}'s number is {phonebook[u_input]}")
    else:
        print(f"{u_input} not found in the phonebook.")

    if u_input in phonebook:
        print(f"{u_input} is in the phonebook.")
    else:
        phonebook[u_input] = '000-000000'
        print(f"{u_input} has been added to the phonebook.")

    print(f"{ph_num}", "has been removed from the phonebook.")
    print("-----------------------------------")
    print("Phonebook contents:")

    for key in phonebook:
        print(f"{key}: {phonebook[key]}")

    print("-----------------------------------")

# Check for KeyError
except KeyError as e:
    print(f"KeyError: {e} - Key not found in the dictionary.")
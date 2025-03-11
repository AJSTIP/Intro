fname = input("Enter your first name: ")    # Prompt the user to enter their first name
lname = input("Enter your last name: ")    # Prompt the user to enter their last name   
phonenumber = input("Enter your phone number: ")    # Prompt the user to enter their phone number

# Check if the first name is empty  
if fname == "":
    print("You must enter your first name.")
# Check if the last name is empty
elif lname == "":
    print("You must enter your last name.")
# Check if the phone number is empty
elif phonenumber == "":
    print("You must enter your phone number.")
# Check if the phone number is not a number
elif not phonenumber.isdigit():
    print("You must enter a number for your phone number.")

# If all the conditions are met, print the user's information
else:
    print(f"First Name: {fname}, Last Name: {lname}, Phone Number: {phonenumber}")
    print("Thank you for entering your information.")

# Prevent the program from closing on its own
input("Press Enter to exit...")
# End of the program
def add(x, y): # Function to add two numbers
    return x + y

def subtract(x, y): # Function to subtract two numbers
    return x - y

def multiply(x, y): # Function to multiply two numbers
    return x * y

def divide(x, y): # Function to divide two numbers
    try:
        return x / y
    except ZeroDivisionError:
        return "Error! Division by zero."

def generate_menu(): # Function to display the calculator menu
    print("Select operation:\n1. Add\n2. Subtract\n3. Multiply\n4. Divide")
    choice = input("Enter choice(1/2/3/4): ")
    return choice

def calculator(): # Main function to run the calculator
    choice = generate_menu()
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1': # If the user selects 1, the add function is called
        print(f"The result is: {add(num1, num2)}")
    elif choice == '2': # If the user selects 2, the subtract function is called
        print(f"The result is: {subtract(num1, num2)}")
    elif choice == '3': # If the user selects 3, the multiply function is called
        print(f"The result is: {multiply(num1, num2)}")
    elif choice == '4': # If the user selects 4, the divide function is called
        print(f"The result is: {divide(num1, num2)}")
    else: # If the user selects an invalid option, an error message is displayed
        print("Invalid input")

calculator() # Call the calculator function

input("Press Enter to exit...")
# End of the program

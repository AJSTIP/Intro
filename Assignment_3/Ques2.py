# Define the list of items
Items = ['Apple', 'Banana', 'Orange', 
         'Grapes', 'Mango', 'Pineapple', 
         'Watermelon', 'Peach', 'Strawberry', 'Cherry']

# Initialize an empty basket
Basket = []

# Start the loop
while True:
    print("\nSelect an item by entering the number next to it:")
    
    # Display the items with an index
    for i, item in enumerate(Items, 1):
        print(f"{i}. {item}")
    
    # Prompt the user to select an item or exit
    selection = int(input("Enter the number of the item you want to add to the basket (Enter 0 to exit): "))
    
    if selection == 0:
        break  # Exit the loop if user selects 0
    
    # Check if the selection is valid
    if 1 <= selection <= len(Items):
        Basket.append(Items[selection - 1])  # Add the selected item to the basket
        print(f"Added {Items[selection - 1]} to your basket.")
    else:
        print("Invalid selection. Please try again.")

# Print the final basket
print("\nYour basket contains:")
for item in Basket:
    print(item)

input("Press Enter to exit...")
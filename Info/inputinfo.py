import main as m

def main():
    my_info = m.Information("John Doe", 30, "123 Main St", "555-1234")
    fr_info = m.Information("Jane Smith", 28, "456 Elm St", "555-5678")
    
    print("Information about John Doe:")
    my_info.display()
    
    print("\nInformation about Jane Smith:")
    fr_info.display()

def display_info(info):
    print(f"Name: {info.name}, Age: {info.age}, Address: {info.address}, Phone: {info.phone}")
    
if __name__ == "__main__":
    main()

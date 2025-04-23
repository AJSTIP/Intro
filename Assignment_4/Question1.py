# Person class
class Person:
    def __init__(self, name, address, telephone):
        self.name = name
        self.address = address
        self.telephone = telephone

    def __str__(self):
        return f"Name: {self.name}, Address: {self.address}, Telephone: {self.telephone}"

# Customer class (subclass of Person)
class Customer(Person):
    def __init__(self, name, address, telephone, customer_number, mailing_list):
        super().__init__(name, address, telephone)
        self.customer_number = customer_number
        self.mailing_list = mailing_list

    def __str__(self):
        mailing_list_status = "Yes" if self.mailing_list else "No"
        return (super().__str__() +
                f", Customer Number: {self.customer_number}, Mailing List: {mailing_list_status}")

# Demonstration of the Customer class
def main():
    # Create an instance of the Customer class
    customer = Customer("John Hancock", "123 Fiscal Ave.", "555-1234", 1001, True)
    
    # Display the customer's information
    print(customer)

if __name__ == "__main__":
    main()
    input("Press Enter to exit...")
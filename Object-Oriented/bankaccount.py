class Bankaccount():
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount} \nNew balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: {amount} \nNew balance: {self.balance}")
        elif amount > self.balance:
            print("The Withdrawal amount exceeds balance.")
        else:
            print("Withdrawal amount exceeds balance or is invalid.")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Bank Account Balance: {self.balance}" # This method returns a string representation of the object, which is useful for printing the object directly.

def main():
    account = Bankaccount(1000)
    print(account)  # Uses the __str__ method to display the account balance

    account.deposit(500)
    print(account)  # Updated balance after deposit
    
    account.withdraw(200)
    print(account)  # Updated balance after withdrawal
    
    account.withdraw(2000)  # Invalid withdrawal
    print(account)  # Balance remains unchanged

if __name__ == "__main__":
    main()
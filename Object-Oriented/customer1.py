import bankaccount

start_balance = float(input("Enter the starting balance: "))
account = bankaccount.Bankaccount(start_balance)
print(f"\nInitial balance: {account.get_balance()}")

balance_deposit = float(input("Enter the amount to deposit: "))
account.deposit(balance_deposit)
print(f"New balance after deposit: {account.get_balance()}")

balance_withdraw = float(input("Enter the amount to withdraw: "))
account.withdraw(balance_withdraw)
print(f"New balance after withdrawal: {account.get_balance()}")
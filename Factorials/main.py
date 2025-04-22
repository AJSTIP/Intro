def main():
    num = int(input("Enter a number to calculate its factorial: "))
    result = factorial(num)
    print(f"The factorial of {num} is {result}")

def factorial(num):
    return 1 if num == 0 else num * factorial(num - 1)

if __name__ == "__main__":
    main()
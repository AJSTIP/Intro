def gcd(x, y):
    # Iterative approach to avoid recursion depth issues
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    # Handle edge case where one or both numbers are zero
    return 0 if x == 0 or y == 0 else x * y // gcd(x, y)

def get_positive_integer(prompt):
    while True:
        try:
            num = int(input(prompt))
            if num < 0:
                raise ValueError("Number must be non-negative.")
            return num
        except ValueError as e:
            print(e)

def main():
    x = get_positive_integer("Enter first number: ")
    y = get_positive_integer("Enter second number: ")
    print(f"Greatest Common Denominator of {x} and {y} is {gcd(x, y)}")
    print(f"Least Common Multiple of {x} and {y} is {lcm(x, y)}")

if __name__ == "__main__":
    main()
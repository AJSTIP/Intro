def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
    
def main():
        n = int(input("Enter a positive integer: "))
        print("Fibonacci sequence:")
        for i in range(n + 1):
            print(f"The {i}th Fibonacci number is: {fib(i)}")
        
if __name__ == "__main__":
    main()
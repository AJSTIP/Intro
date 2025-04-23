def ackermann(m, n):
    """
    Computes the Ackermann function for given m and n.
    :param m: Non-negative integer
    :param n: Non-negative integer
    :return: Result of the Ackermann function
    """
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))

# Test the function with small values of m and n
if __name__ == "__main__":
    print("Ackermann(0, 0):", ackermann(0, 0))
    print("Ackermann(1, 2):", ackermann(1, 2))
    print("Ackermann(2, 2):", ackermann(2, 2))
    print("Ackermann(3, 3):", ackermann(3, 3))  # Be cautious with larger values as it grows very quickly

    input("Press Enter to exit...")
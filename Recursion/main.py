def sum_range(numlist, start_i, end_i):
    if start_i > end_i:
        return 0
    else:
        return numlist[start_i] + sum_range(numlist, start_i + 1, end_i)
    
def main():
    numlist = [2, 5, 5, 6, 8, 10, 25]
    result = sum_range(numlist, 3, 4)
    print(f"The sum of the list is: {result}")

if __name__ == "__main__":
    main()
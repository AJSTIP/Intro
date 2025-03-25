num = [1,2,3,4,5,6,7,8,9,10]

squares = {item:item ** 2 for item in num}
# The above code is a dictionary comprehension that creates a new dictionary called 'squares'.
# The keys of the dictionary are the numbers from 1 to 10, and the values are the squares of those numbers.
# The 'item' variable represents each number in the 'num' list, and 'item ** 2' calculates the square of that number.

print(squares)

#----------------------------------------------------------------------------------------------------------------------------------

names = ['John', 'Jane', 'Doe', 'Kevin', 'Peter']

name_length = {item:len(item) for item in names}
# The above code is a dictionary comprehension that creates a new dictionary called 'name_length'.
# The keys of the dictionary are the names from the 'names' list, and the values are the lengths of those names.
# The 'item' variable represents each name in the 'names' list, and 'len(item)' calculates the length of that name.

print(name_length)
###
# Tuples are immutable, which means you cannot change the values in a tuple.
# You can access the values in a tuple using their index number.
# The index number starts from 0.
# You cannot remove items from a tuple.
# You cannot add items to a tuple.
# Nothing about the tuple can be manipulated once created.
# Tuples are faster than lists.
# Tuples can be turned into lists, and vice-versa.
###

tuple1 = (1, 2, 3, 4, 5)
list1 = list(tuple1) # Convert tuple to list
print (list1)   

list2 = [6, 7, 8, 9, 10]
tuple2 = tuple(list2) # Convert list to tuple
print (tuple2)
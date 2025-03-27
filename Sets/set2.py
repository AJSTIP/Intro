myset1 = set(['a', 'b', 'c', 'd'])

myset2 = set(['d', 'f', 'g', 'h'])

#result = myset1.intersection(myset2)
#result = myset1 & myset2 
#Both these results give the same output, the & is shorthand for intersection

#result = myset1 | myset2
#result = myset1.union(myset2)
#These also give the same output | is the shorthand for union

#For intersection and union the order does not matter
#----------------------------------------------------------------------------------------------------#

#result = myset1 - myset2 
#For difference order matters which set comes first

result = myset1.symmetric_difference(myset2) 
#Order does not matter for symmetric difference

print(result)
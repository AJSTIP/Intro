myset1 = set(['a', 'b', 'c', 'd', 'e'])

myset2 = set({i for i in myset1 if i < 'c'}) #- This creates a SET definition

myset3 = set([i for i in myset1]) #- This creates a LIST comprehension


print(myset2)
print(myset3)

if myset2 <= myset1:
    print('Is a subset')

if myset1 <= myset2:
    print('Is a subset')
#Subsets work both ways as long as they have the same information

if myset2 <= myset1:
    print('Is a superset') #The bigger set is the superset


myset = set(['apple', 'banana', 'cherry'])

# Adding a single element
myset.add('orange')

# Adding multiple elements using update
myset.update(['grape', 'mango', 'pineapple'])

# Discarding 'apple' from the set
myset.discard('apple')

#myset.remove('grape')

if 'grape' in myset:
    print('Grape is in the set, good choice')
else:
    print('Grape is not in the list, too bad')

print(myset)
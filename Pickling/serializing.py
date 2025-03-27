import pickle

phonebook = {'Chris': '555-7845', 'John': '777-0987',
             'Steve': '444-3456', 'Denise': '111-3214'}

emp = {'YSU': 12265, 'Youngstown': 4587}


phonefile = open('contacts.dat', 'wb') #Dat instead of txt to differentiate between binary and text

pickle.dump(phonebook, phonefile)
pickle.dump(emp, phonefile)

phonefile.close
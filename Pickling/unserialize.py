import pickle

phonefile = open('contacts.dat', 'rb') #Dat instead of txt to differentiate between binary and text

contact = pickle.load(phonefile)

emp = pickle.load(phonefile)

print(contact)

print(emp)

phonefile.close
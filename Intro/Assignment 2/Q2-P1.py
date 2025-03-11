# Prompt the user to enter 3 names
names = []
for i in range(3):
    name = input(f"Enter name {i+1}: ")
    names.append(name)

file = open("names.txt", "w")
for name in names:
    file.write(name + "\n")
file.close()

print("Names have been written to names.txt")
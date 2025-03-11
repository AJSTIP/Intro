# Open the file "names.txt" and read the names
file = open("names.txt", "r")
line = file.readline()
while line:
    print(line.strip())
    line = file.readline()
file.close()
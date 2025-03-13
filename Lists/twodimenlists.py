import random as rnd

n_rows = 3
n_cols = 3

list1 = [[85, 90, 78],
         [90, 93, 82],
         [78, 85, 80]] 

for row in range(n_rows):
    for col in range(n_cols):
        list1[row][col] = rnd.randint(1, 100)

print(list1)
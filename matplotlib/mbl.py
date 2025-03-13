import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# Create some data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Create a figure and axis
plt.plot(x, y, marker='o', linestyle='--', color='r', label='Prime Numbers')
plt.legend()

# Add a title
plt.title('Prime Numbers')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Show the plot
plt.show()

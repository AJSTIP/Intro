import matplotlib.pyplot as plt
import numpy as np

# This code creates a simple pie chart using matplotlib
values = [10, 20, 30, 40, 50]

# Define the colors for each slice of the pie chart
colors = ('red', 'blue', 'green', 'yellow', 'purple')

# Create a pie chart
# The autopct parameter formats the percentage display on the pie chart
# The startangle parameter rotates the start of the pie chart
# The shadow parameter adds a shadow effect to the pie chart
# The explode parameter separates the slices for emphasis
plt.pie(values,
        labels=['A', 'B', 'C', 'D', 'E'], 
        colors=colors, 
        autopct='%1.1f%%', 
        startangle=90,
        explode=(0.3, 0, 0, 0.1, 0), 
        shadow=True)

# Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')  

# Add a title to the pie chart
plt.title('Pie Chart Example')

# Display the pie chart
plt.show()
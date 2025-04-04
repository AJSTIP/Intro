import matplotlib.pyplot as plt
import numpy as np

# Example data for the bar chart
left_edges = np.array([0, 10, 20, 30, 40, 50])  # Left edges of the bars
height = np.array([1, 2.75, 3.25, 3.50, 4.45, 5])  # Heights of the bars

# Width of the bars
width = 8  # Adjusted width to avoid overlap

# Create a bar chart with the left edges aligned
plt.bar(left_edges, height, width=width, align='edge', color='blue', edgecolor='black')

# Adding labels and title
plt.xlabel('Gas Used (in m³)')
plt.ylabel('Minimum Gas Price (in $)')
plt.title('Gas Price vs Gas Used')

# Set the x-ticks to be the left edges
plt.xticks(left_edges)
# Set the y-ticks to be spaced by 1 unit
plt.yticks(np.arange(0, height.max() + 1, 1))

# Add a horizontal line at y=0 for reference
plt.axhline(0, color='black', linewidth=0.8)

# Add a vertical line at each left edge for better visibility
for edge in left_edges:
    plt.axvline(x=edge, color='gray', linestyle='--', linewidth=0.5)

# Set the limits for x and y axes
plt.xlim(left_edges[0] - width, left_edges[-1] + width)
plt.ylim(0, height.max() + 1)

# Add a grid for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Display the plot
plt.show()


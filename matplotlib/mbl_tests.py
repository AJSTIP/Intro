import numpy as np
import matplotlib.pyplot as plt

# Generate data using numpy
x = np.linspace(0, 2 * np.pi, 100)  # 100 points from 0 to 2*pi
y = np.sin(x)

# Create a plot using matplotlib
plt.plot(x, y, label='Sine Wave')

# Add title and labels
plt.title('Sine Wave')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Add a legend
plt.legend()

# Show the plot
plt.show()